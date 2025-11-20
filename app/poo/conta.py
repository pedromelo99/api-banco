from abc import ABC, abstractmethod
from typing import List


class Conta(ABC):
    """Classe abstrata base para contas bancárias"""
    
    def __init__(self, titular: str):
        self._titular = titular
        self._saldo = 0.0
        self._transacoes = []
    
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
