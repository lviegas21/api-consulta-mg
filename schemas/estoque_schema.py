from pydantic import BaseModel

class EstoquePost(BaseModel):
    quantidade: int
    fk_produto: int

class EstoqueListOutput(BaseModel):
    id: int
    quantidade: int
    fk_produto: int


    class Config:
        orm_mode = True