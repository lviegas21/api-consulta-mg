from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Endereco(Base):
    __tablename__ = 'endereco'
    id = Column(Integer, primary_key=True, autoincrement=True)
    rua = Column(String)
    numero = Column(Integer)
    bairro = Column(String)
    cep = Column(String)
    complemento = Column(String)
    fk_cliente = Column(Integer, ForeignKey('cliente.id'))
