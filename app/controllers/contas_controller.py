from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import ContaModel, TransacaoModel
from app.poo.conta_corrente import ContaCorrente
from app.poo.conta_poupanca import ContaPoupanca
from app.poo.transacao import Deposito, Saque
from datetime import datetime


def criar_conta(db: Session, titular: str, tipo: str, limite_especial: float = 0.0):
    """Cria uma nova conta no banco de dados"""
    
    # Validação do tipo
    if tipo not in ["corrente", "poupanca"]:
        raise HTTPException(status_code=400, detail="Tipo de conta inválido")
    
    # Criar objeto POO da conta
    if tipo == "corrente":
        conta_obj = ContaCorrente(titular, limite_especial)
    else:
        conta_obj = ContaPoupanca(titular)
    
    # Criar registro no banco
    conta_db = ContaModel(
        titular=titular,
        tipo=tipo,
        saldo=0.0,
        limite_especial=limite_especial if tipo == "corrente" else 0.0
    )
    
    db.add(conta_db)
    db.commit()
    db.refresh(conta_db)
    
    return conta_db


def obter_conta(db: Session, conta_id: int):
    """Busca uma conta por ID"""
    conta = db.query(ContaModel).filter(ContaModel.id == conta_id).first()
    
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    
    return conta


def listar_contas(db: Session):
    """Lista todas as contas"""
    contas = db.query(ContaModel).all()
    return contas


def deletar_conta(db: Session, conta_id: int):
    """Deleta uma conta"""
    conta = obter_conta(db, conta_id)
    
    db.delete(conta)
    db.commit()
    
    return {"mensagem": "Conta deletada com sucesso"}


def depositar(db: Session, conta_id: int, valor: float):
    """Realiza um depósito na conta usando classe Transacao"""
    
    # Buscar conta no banco
    conta_db = obter_conta(db, conta_id)
    
    # Criar objeto POO correspondente
    if conta_db.tipo == "corrente":
        conta_obj = ContaCorrente(conta_db.titular, conta_db.limite_especial)
    else:
        conta_obj = ContaPoupanca(conta_db.titular)
    
    conta_obj.saldo = conta_db.saldo
    
    try:
        # Criar objeto Deposito (classe abstrata Transacao)
        deposito = Deposito(valor)
        
        # Executar depósito usando polimorfismo
        deposito.executar(conta_obj)
        
        # Atualizar banco de dados
        conta_db.saldo = conta_obj.saldo
        
        # Criar registro de transação
        transacao = TransacaoModel(
            conta_id=conta_id,
            tipo=deposito.get_tipo(),
            valor=valor,
            data=deposito.data
        )
        
        db.add(transacao)
        db.commit()
        db.refresh(conta_db)
        
        return {
            "mensagem": "Depósito realizado com sucesso",
            "saldo": conta_db.saldo
        }
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


def sacar(db: Session, conta_id: int, valor: float):
    """Realiza um saque na conta usando classe Transacao"""
    
    # Buscar conta no banco
    conta_db = obter_conta(db, conta_id)
    
    # Criar objeto POO correspondente
    if conta_db.tipo == "corrente":
        conta_obj = ContaCorrente(conta_db.titular, conta_db.limite_especial)
    else:
        conta_obj = ContaPoupanca(conta_db.titular)
    
    conta_obj.saldo = conta_db.saldo
    
    try:
        # Criar objeto Saque (classe abstrata Transacao)
        saque = Saque(valor)
        
        # Executar saque (usa método sacar da conta)
        conta_obj.sacar(valor)
        
        # Atualizar banco de dados
        conta_db.saldo = conta_obj.saldo
        
        # Criar registro de transação
        transacao = TransacaoModel(
            conta_id=conta_id,
            tipo=saque.get_tipo(),
            valor=valor,
            data=saque.data
        )
        
        db.add(transacao)
        db.commit()
        db.refresh(conta_db)
        
        return {
            "mensagem": "Saque realizado com sucesso",
            "saldo": conta_db.saldo
        }
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
