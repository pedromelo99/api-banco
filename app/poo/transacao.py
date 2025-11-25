from abc import ABC, abstractmethod
from datetime import datetime


class Transacao(ABC):
    """Classe abstrata base para transações bancárias"""
    
    def __init__(self, valor: float):
        if valor <= 0:
            raise ValueError("Valor da transação deve ser maior que zero")
        self._valor = valor
        self._data = datetime.now()
    
    @property
    def valor(self) -> float:
        return self._valor
    
    @property
    def data(self) -> datetime:
        return self._data
    
    @abstractmethod
    def executar(self, conta) -> bool:
        """Executa a transação (método abstrato)"""
        pass
    
    @abstractmethod
    def get_tipo(self) -> str:
        """Retorna o tipo da transação"""
        pass


class Deposito(Transacao):
    """Transação de depósito"""
    
    def executar(self, conta) -> bool:
        """Executa o depósito na conta"""
        conta.saldo += self._valor
        return True
    
    def get_tipo(self) -> str:
        return "deposito"


class Saque(Transacao):
    """Transação de saque"""
    
    def executar(self, conta) -> bool:
        """Executa o saque da conta"""
        # Validação específica para cada tipo de conta
        # é feita no método sacar() da conta
        return conta.sacar(self._valor)
    
    def get_tipo(self) -> str:
        return "saque"


class Rendimento(Transacao):
    """Transação de rendimento (poupança)"""
    
    def executar(self, conta) -> bool:
        """Aplica rendimento na conta"""
        conta.saldo += self._valor
        return True
    
    def get_tipo(self) -> str:
        return "rendimento"
