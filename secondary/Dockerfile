# Використовуємо Python 3.11
FROM python:3.11-slim

# Копіюємо файли додатку
WORKDIR /app
COPY . /app

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Запускаємо додаток
CMD ["python", "app.py"]
