# Arquitetura MVC - Introdução

> 📚 **Projeto de estudos** desenvolvido durante o Módulo 5 do curso da [Rocketseat](https://www.rocketseat.com.br/).

## Sobre o projeto

API REST simples para gerenciar **pessoas** e **pets**, criada para praticar o padrão de arquitetura **MVC (Model-View-Controller)**:

- **Models** (`src/models`): entidades e repositórios que acessam o banco de dados SQLite.
- **Views** (`src/views`): recebem as requisições HTTP e montam as respostas.
- **Controllers** (`src/controllers`): concentram as regras de negócio.

O projeto também tem validação de dados, tratamento de erros HTTP (400, 404 e 422), composers que montam as dependências de cada rota e testes unitários.

### Rotas

| Método | Rota                 | Descrição                    |
| ------ | -------------------- | ---------------------------- |
| GET    | `/pets`              | Lista todos os pets          |
| DELETE | `/pets/<name>`       | Remove um pet pelo nome      |
| POST   | `/people`            | Cadastra uma pessoa          |
| GET    | `/people/<id>`       | Busca uma pessoa pelo ID     |

## Tecnologias

- Python
- Flask + Flask-CORS
- SQLAlchemy
- SQLite
- Pydantic
- Pytest + pytest-mock + mock-alchemy
- Pylint + pre-commit

## Como executar

```bash
# instalar as dependências
pip install -r requirements.txt

# criar o banco (storage.db) a partir do script em init/schemas.sql
sqlite3 storage.db < init/schemas.sql

# iniciar o servidor (http://localhost:3000)
python app.py

# rodar os testes
pytest
```
