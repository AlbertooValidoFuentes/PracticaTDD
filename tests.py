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
        self.assertEqual(contador.valorLimite, 10)
        self.assertEqual(contador.valorInicial, 2)
        self.assertEqual(contador.valorIncremento, 2)
    
    def test_valores_iniciales(self):
        '''
            Funcion que contiene el test para comprobar que el valor inicial y incremento es correcto. 
        '''
        contador = Contador(10)
        self.assertEqual(contador.valorInicial, 0)
        self.assertEqual(contador.valorIncremento, 1)
        
    def test_valores_noCambian(self):
        '''
            Funcion que contiene el test para comprobar que el valor inicial y incremento no cambian. 
        '''
        contador = Contador(10, 2, 2)
        contador.valorInicial = 3
        contador.valorIncremento = 3
        contador.valorLimite = 3
        self.assertEqual(contador.valorInicial, 2)
        self.assertEqual(contador.valorIncremento, 2)
        self.assertEqual(contador.valorLimite, 10)
    
if __name__ == '__main__':
    unittest.main()