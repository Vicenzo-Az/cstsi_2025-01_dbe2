# CSTSI_2025-01_DBE2

## Índice

- [Visão Geral](#visão-geral)  
- [Funcionalidades](#funcionalidades)  
- [Tecnologias](#tecnologias)  
- [Requisitos](#requisitos)  
- [Instalação](#instalação)  
- [Configuração de Variáveis de Ambiente](#configuração-de-variáveis-de-ambiente)  
- [Execução com Docker](#execução-com-docker)  
- [Estrutura do Projeto](#estrutura-do-projeto)  
- [Modelos de Dados (Models)](#modelos-de-dados-models)  
- [Serializadores (Serializers)](#serializadores-serializers)  
- [Rotas e Endpoints](#rotas-e-endpoints)  
- [Factories e Testes](#factories-e-testes)
- [Seeders](#seeders)
- [Exemplos de Uso](#exemplos-de-uso)  

---

## Visão Geral

Este repositório contém o projeto desenvolvido na disciplina **Desenvolvimento Back-End II** (4º semestre do CSTSI), ministrada pela Prof. Gill Velleda Gonzales.
Trata-se de uma **API REST** em **Django 5.2** + **Django REST Framework**, com autenticação via **JWT** (biblioteca `rest_framework_simplejwt`), destinada a gerenciar:

- **DataSources** (fontes de dados externas, CSV, bancos etc.)
- **Dashboards** (configurações de visualização de gráficos baseadas nas fontes)
- **AnalysisReports** (relatórios analíticos, com possibilidade de geração por IA)

---

## Funcionalidades

1. **CRUD** completo de DataSources, Dashboards e AnalysisReports
2. **Filtragem** dos recursos pelo usuário autenticado
3. Autenticação via **JWT** com endpoints para obtenção e refresh de tokens
4. Endpoint para retornar dados do usuário corrente (`/api/v1/auth/user/`)
5. Configuração de CORS para permitir chamadas de front‑ends (ex.: `localhost:3000`)

---

## Tecnologias

- **Linguagem**: Python 3.11  
- **Framework**: Django 5.2, Django REST Framework  
- **Autenticação**: `djangorestframework-simplejwt`  
- **Banco de Dados**: PostgreSQL 14 (via Docker)  
- **Containerização**: Docker & Docker Compose  
- **Outros**: `python-dotenv`, `corsheaders`  

---

## Requisitos

- Docker (>= 20.10)  
- Docker Compose (>= 1.29)  
- Variáveis de ambiente definidas em arquivo `.env` (veja seção abaixo)

---

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/Vicenzo-Az/cstsi_2025-01_dbe2.git
   cd cstsi_2025-01_dbe2
    ```

2. Crie um arquivo `.env` na raiz (use o modelo abaixo).
3. Execute com Docker Compose (próxima seção).

---

## Configuração de Variáveis de Ambiente

No arquivo `.env`, defina:

```env
# Django
SECRET_KEY=uma_chave_super_secreta

# PostgreSQL
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=postgres  # nome de serviço no docker-compose
```

---

## Execução com Docker

```bash
# Cria e inicia containers de app e banco
docker-compose up --build -d

# Aguarda logs e verifica
docker-compose logs -f web
```

- A API ficará disponível em `http://localhost:8000/`
- Admin Django: `http://localhost:8000/admin/` (crie superusuário com `docker-compose exec web python manage.py createsuperuser`)

Para parar e remover containers:

```bash
docker-compose down
```

---

## Estrutura do Projeto

```text
├── api/                 # App Django “api”
│   ├── factories.py     # Factories para testes
│   ├── models.py        # Modelos: DataSource, Dashboard, AnalysisReport
│   ├── serializers.py   # Serializers DRF
│   ├── views.py         # ViewSets e APIView
│   └── urls.py          # Rotas do app api/v1/
├── project/             # Configuração do projeto Django
│   ├── settings.py      # Configurações gerais
│   ├── urls.py          # URLs globais
│   └── wsgi.py
├── tcc/                 # App Django “tcc” (front‑end mínimo / landing)
│   └── urls.py          # Páginas estáticas / templates
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── wait-for-postgres.sh
```

---

## 📄 Documentação da API (drf-spectacular)

Para facilitar o consumo e teste da API, foi adicionado **drf-spectacular** para gerar uma spec OpenAPI 3 e disponibilizar uma UI Swagger interativa e um ReDoc do projeto.

- **Swagger‑UI**  
  Acesse: `http://localhost:8000/api/v1/docs/swagger/`  
  → Interface interativa para navegar pelos endpoints e testar requisições.

- **ReDoc**  
  Acesse: `http://localhost:8000/api/v1/docs/redoc/`  
  → Visualização limpa e estruturada da spec OpenAPI 3.

- **Esquema OpenAPI (JSON)**  
  Para integração com ferramentas ou geração de SDKs:
  → GET [http://localhost:8000/schema/](http://localhost:8000/schema/)

### Autenticação

1. Clique em **Authorize** na Swagger‑UI.  
2. Informe seu token JWT no formato:

```markdown
Bearer <seu-token>
```

3. Pronto: agora é possível testar endpoints protegidos diretamente na interface.

---

## Modelos de Dados (Models)

```python
class DataSource(models.Model):
    user = ForeignKey(User)
    name = CharField(max_length=100)
    source_type = CharField(choices=[('CSV','...'),('API','...'),('DB','...')])
    connection_details = JSONField()
    created_at = DateTimeField(auto_now_add=True)

class Dashboard(models.Model):
    user = ForeignKey(User)
    name = CharField(max_length=100)
    description = TextField(blank=True)
    config = JSONField()           # Deve conter chave 'charts'
    data_sources = ManyToManyField(DataSource)
    created_at = DateTimeField(auto_now_add=True)

class AnalysisReport(models.Model):
    user = ForeignKey(User)
    title = CharField(max_length=200)
    content = TextField()
    generated_by_ai = BooleanField(default=False)
    data_sources = ManyToManyField(DataSource)
    created_at = DateTimeField(auto_now_add=True)
```

---

## Serializadores (Serializers)

- **DataSourceSerializer**: valida `source_type`
- **DashboardSerializer**: valida se `config` contém ao menos a chave `'charts'`
- **AnalysisReportSerializer**

---

## Rotas e Endpoints

| Método | Rota                        | Descrição                             |
| ------ | --------------------------- | ------------------------------------- |
| POST   | `/api/v1/token/`            | Obtém `access` e `refresh` tokens JWT |
| POST   | `/api/v1/token/refresh/`    | Atualiza token a partir do `refresh`  |
| GET    | `/api/v1/auth/user/`        | Dados do usuário autenticado          |
| CRUD   | `/api/v1/data-sources/`     | Gerencia DataSources                  |
| CRUD   | `/api/v1/dashboards/`       | Gerencia Dashboards                   |
| CRUD   | `/api/v1/analysis-reports/` | Gerencia AnalysisReports              |

> **Observação**: todos os endpoints de CRUD exigem cabeçalho `Authorization: Bearer <access_token>`.

---

## Factories e Testes

- **Factories**: em `api/factories.py`, usando `factory_boy` e `faker`. São usadas para gerar instâncias de teste.
- **Testes**: rodar com `pytest`, apontando para `settings_test`:

  ```bash
  pytest
  ```

---

## Seeders

Para popular o banco com dados de teste, use o comando customizado `seed`:

```bash
# Usando settings de teste (SQLite em memória)
python manage.py seed --settings=project.settings_test \
    --users 10 \
    --datasources-per-user 4 \
    --dashboards-per-user 3 \
    --reports-per-user 2
```

Valores padrão (sem flags):

- `--users`: 5
- `--datasources-per-user`: 3
- `--dashboards-per-user`: 2
- `--reports-per-user`: 1

O comando aplica migrations automaticamente antes de semear, garantindo tabelas atualizadas.

---

## Exemplos de Uso

### 1. Autenticação e obtenção de token

```bash
curl -X POST http://localhost:8000/api/v1/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"seu_usuario", "password":"sua_senha"}'
```

**Resposta**:

```json
{
  "refresh": "...",
  "access": "..."
}
```

### 2. Criar um DataSource

```bash
curl -X POST http://localhost:8000/api/v1/data-sources/ \
  -H "Authorization: Bearer <access>" \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Minha API Externa",
        "source_type": "API",
        "connection_details": {
          "url": "https://api.exemplo.com/data",
          "api_key": "abcdef12345"
        }
      }'
```

### 3. Listar Dashboards

```bash
curl -X GET http://localhost:8000/api/v1/dashboards/ \
  -H "Authorization: Bearer <access>"
```
