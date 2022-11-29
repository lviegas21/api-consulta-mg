from ..models.models_base import Base
from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantidade = Column(Integer)
    total = Column(Float)
    date_pedido = Column(String)
    fk_cliente = Column(Integer, ForeignKey('cliente.id'))
    fk_endereco = Column(Integer, ForeignKey('endereco.id'))
    fk_produto = Column(Integer, ForeignKey('produto.id'))
    entrega = relationship('Entrega', backref='pedido', lazy='subquery')
