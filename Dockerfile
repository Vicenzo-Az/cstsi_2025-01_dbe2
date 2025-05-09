# Imagem base do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Define variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \  
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências do Python
COPY requirements.txt .

# Instala dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto Django para o container
COPY . .

# Porta exposta (usada pelo Django runserver)
EXPOSE 8000

# Adicione ANTES do comando CMD
COPY wait-for-postgres.sh /app/wait-for-postgres.sh  
RUN chmod +x /app/wait-for-postgres.sh              

# Comando para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]