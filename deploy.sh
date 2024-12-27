#!/bin/bash

# Создаем директорию .streamlit если её нет
mkdir -p /app/.streamlit

# Копируем файл secrets.toml
cat > /app/.streamlit/secrets.toml << 'EOL'
[flowise]
base_url = "https://5bcxe1md.rpcld.com"
api_base_url = "https://5bcxe1md.rpcld.com/api/v1/prediction/"
simple_chat_id = "51b48128-c6ad-410f-93b1-9248b9ff886e"
main_chat_id = "f14084c4-45b9-4575-b604-381275a04471"

[admin]
admin_username = "Remass164"
admin_password = "01122011.Rem/164"

[openrouter]
api_key = "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"
EOL

# Запускаем приложение
streamlit run main.py 