# Técnica: caixa preta (baseada em especificação)
# Nível: teste de unidade
# Tipo: teste funcional
# Divisão de entradas: por classes de equivalência e valor limite

import unittest
from vendedor import Vendedor

class TestCalcularSalarioBase(unittest.TestCase):

    def test_ct01(self):
        vendedor = Vendedor("Victor", 0, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 0.0)
    
    def test_ct02(self):
        vendedor = Vendedor("Victor", 1, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 1500.0)
    
    def test_ct03(self):
        vendedor = Vendedor("Victor", 2, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 1500.0)

    def test_ct04(self):
        vendedor = Vendedor("Victor", 11, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 1500.0)
    
    def test_ct05(self):
        vendedor = Vendedor("Victor", 12, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 1500.0)
    
    def test_ct06(self):
        vendedor = Vendedor("Victor", 13, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 2000.0)
    
    def test_ct07(self):
        vendedor = Vendedor("Victor", 23, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 2000.0)
    
    def test_ct08(self):
        vendedor = Vendedor("Victor", 24, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 2000.0)
    
    def test_ct09(self):
        vendedor = Vendedor("Victor", 25, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 2500.0)
    
    def test_ct10(self):
        vendedor = Vendedor("Victor", 35, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 2500.0)

    def test_ct11(self):
        vendedor = Vendedor("Victor", 36, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 2500.0)
    
    def test_ct12(self):
        vendedor = Vendedor("Victor", 37, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 3000.0)