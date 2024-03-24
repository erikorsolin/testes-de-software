# Técnica: caixa preta (baseada em especificação)
# Nível: teste de unidade
# Tipo: teste funcional
# Divisão de entradas: por classes de equivalência e valor limite

import unittest
from vendedor import Vendedor

class TestCalcularComissao(unittest.TestCase):
    
        def test_ct01(self):
            vendedor = Vendedor("Victor", 0, 0.0)
            self.assertEqual(vendedor.calcular_comissao(), 0.03)
        
        def test_ct02(self):
            vendedor = Vendedor("Victor", 0, 9999.99)
            self.assertEqual(vendedor.calcular_comissao(), 0.03)
        
        def test_ct03(self):
            vendedor = Vendedor("Victor", 0, 10000.0)
            self.assertEqual(vendedor.calcular_comissao(), 0.03)
        
        def test_ct04(self):
            vendedor = Vendedor("Victor", 0, 49999.99)
            self.assertEqual(vendedor.calcular_comissao(), 0.05)
        
        def test_ct05(self):
            vendedor = Vendedor("Victor", 0, 50000.0)
            self.assertEqual(vendedor.calcular_comissao(), 0.05)
        
        def test_ct06(self):
            vendedor = Vendedor("Victor", 0, 50000.01)
            self.assertEqual(vendedor.calcular_comissao(), 0.1)
        
     