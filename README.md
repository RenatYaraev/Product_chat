# Документация проекта AI Chat Assistant

## Обзор проекта

Это многопользовательское веб-приложение для общения с AI-ассистентом, 
построенное на Streamlit с расширенными возможностями управления контекстом и памятью диалогов. 
Приложение поддерживает множество уникальных функций, 
включая многопоточные чаты и административное управление.

## Архитектура приложения

### Основные компоненты

1. **Фронтенд**: Streamlit
2. **База данных**: TinyDB
3. **AI модель**: Together AI API (LLaMA)
4. **Система управления контекстом**: Собственная реализация

### Структура проекта

```
├── pages/
│   ├── admin/
│   │   └── memory.py         # Административная панель управления памятью
│   ├── key_input.py         # Страница активации ключей
│   ├── new_chat.py          # Основной интерфейс чата
│   ├── profile.py           # Профиль пользователя
│   └── registr.py           # Регистрация пользователей
├── utils/
│   ├── chat_database.py     # Управление базой данных чатов
│   ├── context_manager.py   # Управление контекстом диалогов
│   └── utils.py            # Вспомогательные функции
└── main.py                 # Точка входа приложения
```

Этот документ предоставляет полный обзор функциональности приложения и может служить как для документации,
так и для презентации проекта. Он охватывает все ключевые аспекты системы и выделяет её уникальные особенности.

## Ключевые функции

### 1. Система многопоточных чатов

- Создание множества параллельных чатов
- Независимый контекст для каждого чата
- Возможность переключения между чатами
- Сохранение истории диалогов

### 2. Умное управление контекстом

- Анализ истории диалога
- Выделение релевантного контекста
- Адаптивная память для каждого чата
- Настраиваемые промпты для улучшения контекста

### 3. Административные функции

- Управление параметрами модели
- Мониторинг использования
- Настройка системных промптов
- Анализ истории чатов

### 4. Система пользователей

- Регистрация и аутентификация
- Персональные профили
- Управление токенами доступа
- Ограничение количества генераций

## Уникальные особенности

1. **Контекстная память**

   - Интеллектуальный анализ предыдущих сообщений
   - Адаптивное включение контекста в новые сообщения
   - Настраиваемая глубина анализа истории

2. **Гибкая настройка модели**

   - Настройка температуры генерации
   - Управление токенами
   - Контроль повторений
   - Выбор различных моделей

3. **Система токенов**
   - Ограничение использования по токенам
   - Возможность активации дополнительных токенов
   - Мониторинг использования

## Страницы приложения

### 1. Главная страница (main.py)

- Точка входа в приложение
- Авторизация пользователей
- Базовая навигация

### 2. Новый чат (new_chat.py)

- Основной интерфейс общения
- Управление чат-потоками
- Отправка и получение сообщений
- Контекстная память

### 3. Профиль (profile.py)

- Управление личными данными
- Статистика использования
- Управление токенами
- Настройки пользователя

### 4. Административная панель (memory.py)

- Настройка параметров модели
- Управление промптами
- Анализ использования
- Системные настройки

### 5. Регистрация (registr.py)

- Создание новых аккаунтов
- Валидация данных
- Начальная настройка профиля

### 6. Активация ключей (key_input.py)

- Ввод токенов доступа
- Активация дополнительных генераций
- Проверка валидности ключей

## Технические особенности

1. **Безопасность**

   - Хеширование паролей
   - Проверка прав доступа
   - Защита от несанкционированного доступа

2. **Оптимизация**

   - Кэширование контекста
   - Эффективное хранение истории
   - Оптимизированные запросы к API

3. **Масштабируемость**
   - Модульная архитектура
   - Возможность добавления новых функций
   - Поддержка различных моделей AI

## Заключение

Приложение представляет собой комплексное решение для взаимодействия с AI-ассистентом, 
отличающееся от стандартных чат-ботов наличием продвинутой системы управления контекстом, 
многопользовательской архитектурой и гибкими настройками. Особое внимание уделено удобству 
