from app.poo.conta import Conta


class ContaPoupanca(Conta):
    """Conta poupança com rendimento"""
    
    def __init__(self, titular: str):
        super().__init__(titular)
        self._taxa_rendimento = 0.05  # Rendimento de 5% ao mês
    
    def sacar(self, valor: float) -> bool:
        """Saca um valor da conta poupança"""
        if valor <= 0:
            raise ValueError("Valor do saque deve ser maior que zero")
        
        if valor > self._saldo:
            raise ValueError(f"Saldo insuficiente. Disponível: R$ {self._saldo:.2f}")
        
        self._saldo -= valor
        self._transacoes.append({
            "tipo": "saque",
            "valor": valor
        })
        return True
    
    def calcular_rendimento(self) -> float:
        """Calcula rendimento de 5% sobre o saldo"""
        rendimento = self._saldo * self._taxa_rendimento
        return rendimento
    
    def aplicar_rendimento(self) -> float:
        """Aplica o rendimento ao saldo"""
        rendimento = self.calcular_rendimento()
        if rendimento > 0:
            self._saldo += rendimento
            self._transacoes.append({
                "tipo": "rendimento",
                "valor": rendimento
            })
        return rendimento
