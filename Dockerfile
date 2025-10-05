FROM python:3.13-slim

WORKDIR /app

# Instalar dependências do sistema (necessário para psycopg2)
RUN apt-get update && apt-get install -y \
    libpq-dev gcc curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar o uv
RUN pip install --no-cache-dir uv

# Copiar config do projeto
COPY pyproject.toml uv.lock* ./

# Instalar dependências com uv
RUN uv sync

# Copiar código do projeto
COPY . .

EXPOSE 8000

CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]