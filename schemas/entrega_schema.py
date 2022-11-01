from pydantic import BaseModel

class EntregaPost(BaseModel):
    status: str
    fk_pedido: int

class EntregaListOutput(BaseModel):
    id: int
    status: str
    fk_pedido: int


    class Config:
        orm_mode = True