# Mongodb 5.0
## criar banco de dados
use financeirodb;

db;

show collections;
## Criando a Tabela
db.contas.insert({"nome":"belem","valor":900,"descricao":"fatura sobre condominio mes de abril"});

## mostrar
db.contas.find();
## mostrar
db.contas.find().pretty();

show databases;



