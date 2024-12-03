import os
import streamlit as st
import together
import json
from utils.chat_database import ChatDatabase
from tinydb import TinyDB, Query
import time

class ContextManager:
    def __init__(self):
        # Инициализируем Together API для анализа контекста
        os.environ["TOGETHER_API_KEY"] = st.secrets["together"]["api_key"]
        together.api_key = st.secrets["together"]["api_key"]
        
    def get_context(self, username, message, flow_id=None, last_n_messages=10):
        """Получает контекст для сообщения на основе истории конкретного чата"""
        # Определяем правильный ID базы данных чата
        chat_db_name = None
        
        if flow_id:
            # Для new_chat.py - используем ID конкретного чата
            chat_db_name = f"{username}_{flow_id}"
        else:
            # Для app.py - используем main_chat
            chat_db_name = f"{username}_main_chat"
            
        # Инициализируем базу данных для конкретного чата
        chat_db = ChatDatabase(chat_db_name)
        history = chat_db.get_history()
        
        if not history:
            print(f"История чата {chat_db_name} пуста")
            return message
            
        try:
            # Форматируем историю в структурированный диалог
            formatted_history = []
            for msg in history[-last_n_messages:]:  # Берем только последние n сообщений
                role = "Assistant" if msg['role'] == "assistant" else "User"
                formatted_history.append(f"{role}: {msg['content']}")
            
            history_text = "\n".join(formatted_history)
            print(f"Анализ истории для чата {chat_db_name}")
            
            # Создаем промпт для анализа контекста
            context_prompt = f"""[INST] Ты - ассистент с отличной памятью. Проанализируй историю диалога из конкретного чата и создай контекст для нового вопроса.

История текущего чата:
{history_text}

Новый вопрос пользователя:
{message}

Пожалуйста:
1. Проанализируй историю именно этого чата
2. Определи основные темы обсуждения в этом чате
3. Найди связи между предыдущими вопросами и текущим вопросом
4. Выдели информацию, которая важна для ответа на текущий вопрос
5. Создай краткое резюме контекста этого чата

Формат ответа:
1. Основные темы чата: [перечисли темы]
2. Ключевые моменты: [важные детали]
3. Связь с текущим вопросом: [как текущий вопрос связан с контекстом]
4. Релевантная информация: [что важно для ответа]

[/INST]"""

            # Добавляем повторные попытки при сетевых ошибках
            max_retries = 3
            retry_delay = 2
            
            for attempt in range(max_retries):
                try:
                    response = together.Complete.create(
                        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
                        prompt=context_prompt,
                        max_tokens=2048,
                        temperature=0.2,
                        top_p=0.9,
                        top_k=50,
                        repetition_penalty=1.1
                    )
                    
                    if isinstance(response, dict) and 'output' in response:
                        context_analysis = response['output']['choices'][0]['text'].strip()
                        print(f"Получен анализ контекста для чата {chat_db_name}")
                    else:
                        print(f"Неожиданный формат ответа для чата {chat_db_name}")
                        return message
                    
                    if not context_analysis:
                        return message
                    
                    # Формируем финальное сообщение с контекстом
                    enhanced_message = f"""Контекст текущего чата:
{context_analysis}

Текущий вопрос:
{message}

Используя контекст ТОЛЬКО ЭТОГО чата, дай подробный и связный ответ. Убедись, что ответ логически связан с предыдущими темами разговора В ЭТОМ ЧАТЕ."""
                    
                    return enhanced_message
                    
                except (ConnectionError, TimeoutError) as e:
                    if attempt < max_retries - 1:
                        print(f"Попытка {attempt + 1} не удалась для чата {chat_db_name}: {str(e)}")
                        time.sleep(retry_delay)
                        continue
                    else:
                        print(f"Все попытки исчерпаны для чата {chat_db_name}")
                        return message
                        
                except Exception as e:
                    print(f"Ошибка при анализе контекста для чата {chat_db_name}: {str(e)}")
                    return message
                    
        except Exception as e:
            print(f"Ошибка при обработке истории чата {chat_db_name}: {str(e)}")
            return message