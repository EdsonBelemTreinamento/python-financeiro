from model.contas import Contas
from repository.contas_repository import ContasRepository


contas1 = Contas(nome="luciana",valor=500,descricao="cartao de banco")
contas2 = Contas(nome="omar",valor=200,descricao="racao")
repository = ContasRepository()
try:
    print(f"Salvando:{repository.save(contas1)}")
    print(f"Salvando:{repository.save(contas2)}")
    lista_contas = repository.find_all()
    for conta in lista_contas:
        print(conta)
    
    print("ok")
except Exception as error:
    print("error : {error}")