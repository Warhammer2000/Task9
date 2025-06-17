import os
import sys
import argparse
from openai import OpenAI
from dotenv import load_dotenv

try:
    load_dotenv()
except Exception as e:
    print(f"Error loading .env file: {str(e)}")
    sys.exit(1)

try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
    print(f"Error creating OpenAI client: {str(e)}")
    sys.exit(1)

def generate_report(input_data: str) -> str:
    """Генерация отчета через OpenAI API"""
    system_prompt = "Ты опытный аналитик технологических сервисов." 
    user_prompt = f"""
Проанализируй сервис или продукт на основе предоставленной информации. 
Сгенерируй отчет в формате Markdown со следующими разделами:

1. **Краткая история**: Год основания, ключевые этапы
2. **Целевая аудитория**: Основные сегменты пользователей
3. **Ключевые функции**: 2-4 основных возможности
4. **Уникальные преимущества**: Основные отличия от конкурентов
5. **Бизнес модель**: Как сервис зарабатывает деньги
6. **Технологический стек**: Используемые технологии
7. **Сильные стороны**: Заметные преимущества
8. **Слабые стороны**: Ограничения и недостатки

Информация о сервисе: {input_data}
"""

    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "Ошибка: API ключ OpenAI не найден. Создайте файл .env с переменной OPENAI_API_KEY"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка при генерации отчета: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description='Анализатор сервисов')
    parser.add_argument('input', type=str, help='Название сервиса или описание')
    args = parser.parse_args()

    print("\n" + "="*50)
    print(f"Анализируем: {args.input}")
    print("="*50 + "\n")
    
    report = generate_report(args.input)
    print(report)
    
    print("\n" + "="*50)
    print("Отчет готов!")
    print("="*50)

if __name__ == "__main__":
    main()