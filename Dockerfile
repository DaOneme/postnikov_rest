FROM python:3.12-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Установка Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем Poetry в PATH
ENV PATH="$PATH:/root/.local/bin"

WORKDIR /app

# Копируем файлы конфигурации
# COPY pyproject.toml poetry.lock ./
COPY . .

# Устанавливаем зависимости с --no-root
RUN poetry config virtualenvs.create false --local
RUN poetry install --no-root

# CMD [ "/bin/bash" ]
# Команда запуска
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]