# 🪐 Space Oddity

É uma simples aplicação Django conteinerizada, que utiliza como banco de dados uma instancia Postgres tambem conteinerizada. A aplicação é uma ferramenta para contratantes organizarem os processos seletivos com mais facilidade. Possui somente uma tabela com dois campos.

## Como executar
 Na pasta que contem o documento docker-compose.yml executar os comandos
 
 ```sh
 docker-compose build
 ```
```sh
 docker-compose up
 ```
 
## Como acessar
- web-container é o container da aplicação e esta disponivel na url http://localhots:8000
- db-admin-container contem o PgAdmin que foi incluido apenas caso haja a necessidade de vizualizar os dados de forma mais livre, esta disponivel na url http://localhost:15432 com usuario e senha:
    - usuario:  math.artero@gmail.com
    - senha: pgadmin

- As configurações para conectar o pgadmin com o Postgres seguem abaixo:
    - hostname: db-postgres
    - port: 5432
    - usuario: postgres
    - senha: postgresdb

## Popular o banco de dados

Inicialmente não háverá nenhum dado registrado no banco, mas deixei alguns dados já prontos para serem cadastrados. Basta acessar a url http://localhost:8000/populate com os containers rodando para popular o banco de dados.