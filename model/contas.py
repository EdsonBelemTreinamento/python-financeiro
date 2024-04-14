class Contas:
    def __init__(self,id=None, nome=None, valor=None, descricao=None):
        self.id=id
        self.nome=nome
        self.valor=valor
        self.descricao= descricao
    def __str__(self):
        return f"id={self.id}, nome={self.nome}, valor={self.valor}, descricao={self.descricao}"
    
    def toString(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "valor":self.valor,
            "descricao":self.descricao
        }


#contas1 = Contas(nome="edson",valor=100,descricao="sem parar")
#contas2 = Contas(nome="belem",valor=150,descricao="veloe")
#print(contas1.toString())
#print(contas2)

