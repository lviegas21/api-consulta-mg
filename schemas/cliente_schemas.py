from pydantic import BaseModel

class ClientePost(BaseModel):
    nome: str
    cpf: str
    telefone: str
