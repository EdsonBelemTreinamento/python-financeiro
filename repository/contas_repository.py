from pymongo import MongoClient
from bson import ObjectId

class ContasRepository:
    def __init__(self):
        client = MongoClient("mongodb://localhost:27017/financeirodb")
        self.db = client["financeirodb"]
        self.collection = self.db["contas"]
    
    def save(self, contas):
        user_id= self.collection.insert_one({'nome':contas.nome,'valor':contas.valor,'descricao':contas.descricao})
        return str(user_id)
    
    def find_all(self):
        return list(self.collection.find({},{'_id':1,'nome':1,'valor':1,'descricao':1}))
    




