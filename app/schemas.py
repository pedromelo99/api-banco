from pydantic import BaseModel, Field, validator
from typing import Optional, Literal
from datetime import datetime


# Schemas para criar conta
class ContaCreate(BaseModel):
    titular: str = Field(..., min_length=3, description="Nome do titular da conta")
    tipo: Literal["corrente", "poupanca"] = Field(..., description="Tipo de conta")
    limite_especial: Optional[float] = Field(0.0, description="Limite especial para conta corrente")


# Schema para resposta de conta
class ContaResponse(BaseModel):
    id: int
    titular: str
    tipo: str
    saldo: float
    limite_especial: Optional[float] = 0.0

    class Config:
        from_attributes = True


# Schema para operações de depósito/saque
class OperacaoValor(BaseModel):
    valor: float = Field(..., gt=0, description="Valor da operação deve ser maior que zero")


# Schema para transação
class TransacaoResponse(BaseModel):
    id: int
    tipo: str
    valor: float
    data: datetime

    class Config:
        from_attributes = True


# Schema para estatísticas
class EstatisticasResponse(BaseModel):
    total_depositos: float
    total_saques: float
    total_transacoes: int
    saldo_atual: float
