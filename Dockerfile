FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    bash \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry
ENV PATH="$PATH:/root/.local/bin"

WORKDIR /app
COPY . .

RUN poetry config virtualenvs.create false --local
RUN poetry install --no-root

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
