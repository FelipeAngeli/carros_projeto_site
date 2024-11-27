
# Carros API

Carros API é um projeto desenvolvido com Django, projetado para gerenciar informações relacionadas a carros e usuários. O sistema utiliza PostgreSQL como banco de dados, garantindo escalabilidade e desempenho, e está configurado para deploy com uWSGI.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

- **manage.py**: Script principal para gerenciar comandos administrativos do Django.
- **db.sqlite3**: Anteriormente usado como banco de dados, mas agora substituído por PostgreSQL.
- **app**: Diretório principal do projeto.
- **accounts**, **cars**: Aplicações Django específicas para gerenciar contas de usuários e informações sobre carros.
- **requirements.txt**: Dependências do projeto.
- **carros_uwsgi.ini** e **uwsgi_params**: Arquivos de configuração para deploy com uWSGI.
- **media**: Diretório para armazenar arquivos enviados pelo usuário.
- **openai_api**: Indica uma integração com a API da OpenAI.

## Configuração do Ambiente

### Pré-requisitos

Certifique-se de ter instalado:

- Python 3.8 ou superior
- PostgreSQL
- Virtualenv
- Git

### Configuração do Banco de Dados

1. Crie um banco de dados no PostgreSQL:
   ```sql
   CREATE DATABASE carros_db;
   CREATE USER carros_user WITH PASSWORD 'sua_senha_segura';
   ALTER ROLE carros_user SET client_encoding TO 'utf8';
   ALTER ROLE carros_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE carros_user SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE carros_db TO carros_user;
   ```

### Configuração do Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/FelipeAngeli/carros.git
   cd carros
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente no arquivo `.env` (ou método equivalente):
   ```env
   DATABASE_NAME=carros_db
   DATABASE_USER=carros_user
   DATABASE_PASSWORD=sua_senha_segura
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   ```

5. Aplique as migrações ao banco de dados:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

O servidor estará disponível em `http://127.0.0.1:8000/`.

## Endpoints da API

A API oferece os seguintes recursos:

- **Usuários**:
  - Registro, autenticação e gerenciamento de contas.
- **Carros**:
  - Listar, adicionar, atualizar e remover informações de carros.

### Exemplo de Requisição

#### Listar Carros

`GET /api/cars/`

Resposta:
```json
[
  {
    "id": 1,
    "model": "Ford Mustang",
    "year": 2020,
    "price": 30000.00,
    "owner": "user1@example.com"
  }
]
```

## Testes

Para executar os testes do projeto:

1. Certifique-se de que o banco de dados de teste está configurado corretamente.
2. Execute os testes:
   ```bash
   python manage.py test
   ```

## Deploy com uWSGI

O projeto está configurado para ser implantado com uWSGI. Para iniciar o servidor uWSGI:

1. Certifique-se de que as dependências necessárias estão instaladas:
   ```bash
   pip install uwsgi
   ```

2. Execute o servidor uWSGI:
   ```bash
   uwsgi --ini carros_uwsgi.ini
   ```

O projeto estará disponível no endereço configurado no arquivo `carros_uwsgi.ini`.

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das alterações.
4. Envie um pull request.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
