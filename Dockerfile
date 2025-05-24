# Используем образ Python
FROM python:3.12.3-slim-bullseye

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости, включая те, что нужны для psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта
COPY . /app/

# Открываем порт, на котором будет работать сервер Django
EXPOSE 8000

# Команда, которая будет выполняться при запуске контейнера
# Запускаем сервер разработки Django
CMD ["gunicorn", "traffic_light_system.wsgi:application", "--bind", "0.0.0.0:80", "--workers", "3"]
