from abc import ABC, abstractmethod
from typing import List


class Conta(ABC):
    """Classe abstrata base para contas bancárias"""
    
    def __init__(self, titular: str):
        self._titular = titular
        self._saldo = 0.0
        self._transacoes = []  # Lista para armazenar histórico de transações
    
    @property
    def titular(self) -> str:
        return self._titular
    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor: float):
        self._saldo = valor
    
    @property
    def transacoes(self) -> List:
        return self._transacoes
    
    def depositar(self, valor: float) -> bool:
        """Deposita um valor na conta"""
        if valor <= 0:
            raise ValueError("Valor do depósito deve ser maior que zero")
        
        self._saldo += valor
        self._transacoes.append({
            "tipo": "deposito",
            "valor": valor
        })
        return True
    
    def obter_historico_transacoes(self) -> List[dict]:
        """
        Retorna histórico de transações usando estrutura de repetição explícita
        Demonstra uso de loop for para iterar sobre estrutura de dados
        """
        historico = []
        
        # Loop explícito iterando sobre todas as transações
        for transacao in self._transacoes:
            historico.append({
                "tipo": transacao["tipo"],
                "valor": transacao["valor"]
            })
        
        return historico
    
    def calcular_total_movimentado(self) -> dict:
        """
        Calcula totais de depósitos e saques usando estruturas de repetição
        Demonstra iteração com decisão condicional
        """
        total_depositos = 0.0
        total_saques = 0.0
        
        # Iteração sobre transações com estrutura de decisão
        for transacao in self._transacoes:
            if transacao["tipo"] == "deposito":
                total_depositos += transacao["valor"]
            elif transacao["tipo"] == "saque":
                total_saques += transacao["valor"]
        
        return {
            "total_depositos": total_depositos,
            "total_saques": total_saques,
            "quantidade_transacoes": len(self._transacoes)
        }
    
    @abstractmethod
    def sacar(self, valor: float) -> bool:
        """Saca um valor da conta (método abstrato)"""
        pass
    
    @abstractmethod
    def calcular_rendimento(self) -> float:
        """Calcula rendimento da conta (método abstrato)"""
        pass
    
    def obter_saldo(self) -> float:
        """Retorna o saldo atual"""
        return self._saldo
