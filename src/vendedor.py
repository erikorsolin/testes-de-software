class Vendedor:
    def __init__(self, nome: str, meses_contratado: int, valor_em_vendas: float) -> object:
        self.nome = nome
        self.meses_contratado = meses_contratado
        self.valor_em_vendas = valor_em_vendas


    def calcular_salario_base(self) -> float:
        if self.meses_contratado < 12:
            return 1500.0
        elif self.meses_contratado > 12 and self.meses_contratado < 24:
            return 2000.0
        elif self.meses_contratado > 24 and self.meses_contratado < 36:
            return 2500.0
        elif self.meses_contratado > 36:
            return 3000.0
        
    def calcular_comissao(self) -> float:
        if self.valor_em_vendas < 10000.0:
            return 0.03
        elif self.valor_em_vendas > 1000.0 and self.valor_em_vendas < 50000.0:
            return 0.05
        elif self.valor_em_vendas > 50000.0:
            return 0.1
    
    def calcular_salario_total(self) -> float:
        return self.calcular_salario_base() + (self.valor_em_vendas * self.calcular_comissao())