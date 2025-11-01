# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта
COPY . .

# Открываем порт 8000
EXPOSE 8000

# Команда по умолчанию для запуска MkDocs
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]