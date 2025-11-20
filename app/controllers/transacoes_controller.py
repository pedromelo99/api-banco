from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import TransacaoModel, ContaModel
from fastapi import HTTPException


def listar_transacoes(db: Session, conta_id: int):
    """Lista todas as transações de uma conta"""
    
    # Verificar se a conta existe
    conta = db.query(ContaModel).filter(ContaModel.id == conta_id).first()
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    
    # Buscar transações
    transacoes = db.query(TransacaoModel).filter(
        TransacaoModel.conta_id == conta_id
    ).order_by(TransacaoModel.data.desc()).all()
    
    return transacoes


def obter_estatisticas(db: Session, conta_id: int):
    """Obtém estatísticas de uma conta"""
    
    # Verificar se a conta existe
    conta = db.query(ContaModel).filter(ContaModel.id == conta_id).first()
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    
    # Calcular total de depósitos
    total_depositos = db.query(func.sum(TransacaoModel.valor)).filter(
        TransacaoModel.conta_id == conta_id,
        TransacaoModel.tipo == "deposito"
    ).scalar() or 0.0
    
    # Calcular total de saques
    total_saques = db.query(func.sum(TransacaoModel.valor)).filter(
        TransacaoModel.conta_id == conta_id,
        TransacaoModel.tipo == "saque"
    ).scalar() or 0.0
    
    # Contar total de transações
    total_transacoes = db.query(TransacaoModel).filter(
        TransacaoModel.conta_id == conta_id
    ).count()
    
    return {
        "total_depositos": total_depositos,
        "total_saques": total_saques,
        "total_transacoes": total_transacoes,
        "saldo_atual": conta.saldo
    }
