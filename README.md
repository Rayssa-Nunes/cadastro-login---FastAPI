# Projeto de Cadastro e Login de Usuário com FastAPI e SQLAlchemy

Este projeto foi desenvolvido com o propósito de estudo e demonstra uma abstração do processo de cadastro e login de usuários 
utilizando FastAPI para a criação de uma API REST e SQLAlchemy para interagir com um banco de dados PostgreSQL.

## Funcionalidades

- Cadastro de usuários
- Login de usuários
- Uso de SQLAlchemy como ORM para manipulação do banco de dados
- Flexibilidade na escolha do banco de dados de preferência, uma vez que o SQLAlchemy facilita a troca entre diferentes sistemas de gerenciamento de banco de dados.

## Requisitos
Para testar ou utilizar este projeto, é recomendado o uso de um ambiente virtual (Virtualenv) para evitar conflitos com versões de bibliotecas instaladas no sistema.

As principais tecnologias utilizadas são:

- FastAPI
- SQLAlchemy
- psycopg2 (para conexão com PostgreSQL)

Além disso, é fornecido um arquivo requirements.txt para facilitar a instalação das dependências.
Caso deseje utilizar um banco de dados diferente do PostgreSQL, o SQLAlchemy permite essa flexibilidade.

## Instalação e Uso
1. Clone o repositório
2. Navegue até o diretório do projeto
3. Crie um ambiente virtual (recomendado)
4. Ative o ambiente virtual
5. Instale as dependências: `pip install -r requirements.txt`
6. Execute o servidor: `uvicorn main:app --reload`

O servidor estará em execução em http://localhost:8000. 
Você pode acessar a documentação interativa da API em http://localhost:8000/docs e testar os endpoints disponíveis.
