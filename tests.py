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
    
    

if __name__ == '__main__':
    unittest.main()