import unittest
from Contador import Contador

class TestContador(unittest.TestCase):
    
    '''
        Clase para hacer los test  de la clase Contador (Contador.py)
    '''
    
    def test_constructor(self):
        '''
            Funcion que contiene el test para comprobar que el constructor recoge correctamente los parámetros. 
        '''
        contador = Contador(10, 2, 2)
        self.assertEqual(contador.getValorLimite(), 10)
        self.assertEqual(contador.getValorInicial(), 2)
        self.assertEqual(contador.getValorIncremento(), 2)
    
    def test_valores_iniciales(self):
        '''
            Funcion que contiene el test para comprobar que el valor inicial y incremento es correcto. 
        '''
        contador = Contador(10)
        self.assertEqual(contador.getValorInicial(), 0)
        self.assertEqual(contador.getValorIncremento(), 1)
        
    def test_valores_noCambian(self):
        '''
            Funcion que contiene el test para comprobar que el valor inicial, incremento y limite no cambian. 
        '''
        contador = Contador(10, 2, 2)
        contador.__valorInicial = 3
        contador.__valorIncremento = 3
        contador.__valorLimite = 3
        self.assertEqual(contador.getValorInicial(), 2)
        self.assertEqual(contador.getValorIncremento(), 2)
        self.assertEqual(contador.getValorLimite(), 10 )
    
    def test_incrementar(self):
        '''
            Funcion que contiene el test para comprobar que el contador incrementa correctamente. 
        '''
        contador = Contador(10, 2, 2)
        contador.incrementar()
        self.assertEqual(contador.contador, 4)
        contador.incrementar()
        self.assertEqual(contador.contador, 6)
        contador.incrementar()
        self.assertEqual(contador.contador, 8)
        contador.incrementar()
        self.assertEqual(contador.contador, 10)
        contador.incrementar()
        self.assertEqual(contador.contador, 2)
        
if __name__ == '__main__':
    unittest.main()