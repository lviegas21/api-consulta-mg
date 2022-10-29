from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String)
    preco = Column(Float)
