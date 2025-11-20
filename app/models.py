from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class ContaModel(Base):
    """Modelo da tabela de contas"""
    __tablename__ = "contas"

    id = Column(Integer, primary_key=True, index=True)
    titular = Column(String, nullable=False)
    tipo = Column(String, nullable=False)  # 'corrente' ou 'poupanca'
    saldo = Column(Float, default=0.0)
    limite_especial = Column(Float, default=0.0)  # Usado apenas para conta corrente
    
    # Relacionamento com transações
    transacoes = relationship("TransacaoModel", back_populates="conta", cascade="all, delete-orphan")


class TransacaoModel(Base):
    """Modelo da tabela de transações"""
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    conta_id = Column(Integer, ForeignKey("contas.id"), nullable=False)
    tipo = Column(String, nullable=False)  # 'deposito', 'saque', 'rendimento'
    valor = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.now)
    
    # Relacionamento com conta
    conta = relationship("ContaModel", back_populates="transacoes")
