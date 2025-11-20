from app.poo.conta import Conta


class ContaCorrente(Conta):
    """Conta corrente com limite especial e taxa"""
    
    def __init__(self, titular: str, limite_especial: float = 0.0):
        super().__init__(titular)
        self._limite_especial = limite_especial
        self._taxa = 0.10  # Taxa de 10% sobre operações
    
    @property
    def limite_especial(self) -> float:
        return self._limite_especial
    
    def sacar(self, valor: float) -> bool:
        """Saca um valor da conta corrente"""
        if valor <= 0:
            raise ValueError("Valor do saque deve ser maior que zero")
        
        # Verifica se há saldo suficiente (incluindo limite especial)
        saldo_disponivel = self._saldo + self._limite_especial
        
        if valor > saldo_disponivel:
            raise ValueError(f"Saldo insuficiente. Disponível: R$ {saldo_disponivel:.2f}")
        
        self._saldo -= valor
        self._transacoes.append({
            "tipo": "saque",
            "valor": valor
        })
        return True
    
    def calcular_rendimento(self) -> float:
        """Conta corrente não tem rendimento"""
        return 0.0
    
    def aplicar_taxa(self) -> float:
        """Aplica taxa sobre o saldo"""
        taxa_valor = self._saldo * self._taxa
        return taxa_valor
