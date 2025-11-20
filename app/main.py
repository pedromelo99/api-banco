from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import engine, get_db, Base
from app import schemas
from app.controllers import contas_controller, transacoes_controller

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Criar aplicação FastAPI
app = FastAPI(
    title="API Banking",
    description="API de sistema bancário com POO",
    version="1.0.0"
)


@app.get("/")
def read_root():
    """Rota raiz da API"""
    return {
        "mensagem": "Bem-vindo à API Banking!",
        "versao": "1.0.0",
        "endpoints": {
            "contas": "/contas",
            "documentacao": "/docs"
        }
    }


# ==================== ENDPOINTS DE CONTAS ====================

@app.post("/contas", response_model=schemas.ContaResponse, status_code=201)
def criar_conta(conta: schemas.ContaCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova conta bancária
    
    - **titular**: Nome do titular da conta
    - **tipo**: 'corrente' ou 'poupanca'
    - **limite_especial**: Limite especial (apenas para conta corrente)
    """
    return contas_controller.criar_conta(
        db=db,
        titular=conta.titular,
        tipo=conta.tipo,
        limite_especial=conta.limite_especial or 0.0
    )


@app.get("/contas", response_model=List[schemas.ContaResponse])
def listar_contas(db: Session = Depends(get_db)):
    """Lista todas as contas bancárias"""
    return contas_controller.listar_contas(db=db)


@app.get("/contas/{conta_id}", response_model=schemas.ContaResponse)
def obter_conta(conta_id: int, db: Session = Depends(get_db)):
    """Busca uma conta específica por ID"""
    return contas_controller.obter_conta(db=db, conta_id=conta_id)


@app.delete("/contas/{conta_id}")
def deletar_conta(conta_id: int, db: Session = Depends(get_db)):
    """Deleta uma conta bancária"""
    return contas_controller.deletar_conta(db=db, conta_id=conta_id)


@app.post("/contas/{conta_id}/deposito")
def depositar(conta_id: int, operacao: schemas.OperacaoValor, db: Session = Depends(get_db)):
    """
    Realiza um depósito em uma conta
    
    - **valor**: Valor a ser depositado (deve ser maior que zero)
    """
    return contas_controller.depositar(db=db, conta_id=conta_id, valor=operacao.valor)


@app.post("/contas/{conta_id}/saque")
def sacar(conta_id: int, operacao: schemas.OperacaoValor, db: Session = Depends(get_db)):
    """
    Realiza um saque de uma conta
    
    - **valor**: Valor a ser sacado (deve ser maior que zero)
    """
    return contas_controller.sacar(db=db, conta_id=conta_id, valor=operacao.valor)


# ==================== ENDPOINTS DE TRANSAÇÕES ====================

@app.get("/contas/{conta_id}/transacoes", response_model=List[schemas.TransacaoResponse])
def listar_transacoes(conta_id: int, db: Session = Depends(get_db)):
    """Lista todas as transações de uma conta"""
    return transacoes_controller.listar_transacoes(db=db, conta_id=conta_id)


@app.get("/contas/{conta_id}/estatisticas", response_model=schemas.EstatisticasResponse)
def obter_estatisticas(conta_id: int, db: Session = Depends(get_db)):
    """Obtém estatísticas financeiras de uma conta"""
    return transacoes_controller.obter_estatisticas(db=db, conta_id=conta_id)


# ==================== INICIALIZAÇÃO ====================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
