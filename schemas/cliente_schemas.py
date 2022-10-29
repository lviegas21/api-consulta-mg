from pydantic import BaseModel

class ClientePost(BaseModel):
    nome: str
    cpf: str
    telefone: str

class StandardOutput(BaseModel):
    message: str

class ErrorOutput(BaseModel):
    detail: str

class ClienteListOutput(BaseModel):
    id: int
    nome: str
    cpf: str
    telefone: str

    class Config:
        orm_mode = True