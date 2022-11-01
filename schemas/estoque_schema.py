from pydantic import BaseModel

class EstoquePost(BaseModel):
    quantidade: int
    fk_produto: int

class PedidoListOutput(BaseModel):
    id: int
    quantidade: int
    fk_produto: int


    class Config:
        orm_mode = True