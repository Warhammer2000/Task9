# Service Analyzer

Консольное приложение для генерации аналитических отчетов о сервисах с использованием OpenAI API.

## 📋 Требования
- Python 3.8+
- Действующий OpenAI API ключ (уровень доступа GPT-4)
- Учетная запись на [platform.openai.com](https://platform.openai.com/)

## 🛠️ Установка
1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/репозиторий.git
cd репозиторий

Создайте и активируйте виртуальное окружение:

bash
python -m venv venv
# Для Windows:
venv\Scripts\activate
# Для Linux/MacOS:
source venv/bin/activate
Установите зависимости:

bash
pip install -r requirements.txt
Создайте файл .env и добавьте API ключ:

env
OPENAI_API_KEY=ваш_ключ_здесь
🚀 Использование
Базовый запуск:
python service_analyzer.py "Название сервиса"
Пример:

python service_analyzer.py "Notion"