from ..models.models_base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
class PedidoModel(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantidade = Column(Integer)
    total = Column(Float)
    data = Column(String)
    fk_cliente = Column(Integer, ForeignKey('cliente.id'))
    fk_endereco = Column(Integer, ForeignKey('endereco.id'))
    fk_produto = Column(Integer, ForeignKey('produto.id'))
