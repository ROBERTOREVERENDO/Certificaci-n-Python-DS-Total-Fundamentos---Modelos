def POTENCIA (BAS,POT):
    """
    DOCUMENTACIÓN DE LA FUNCIÓN POTENCIA:
        AUTOR: BJNM
        FECHA DE MODIFICACIÓN/CREACIÓN:
            * V1.0 --> 25/12/2021 (BJNM)
            * V1.1 --> 25/12/2021 (ABCD) 
        PARÁMETROS: BAS,POT (REALES)
        RETORNO: BAS**POT
        EXPLICACIÓN: ESTA ES UNA FUNCIÓN SENCILLA EXPLICATIVA
    
    >>> POTENCIA("HOLA","CHAU")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
    
    """
    return BAS ** POT

import unittest
import doctest

class PRUEBA_UNITARIA(unittest.TestCase):
    def test(self):
        self.assertEqual(POTENCIA(4,2) , 17)

if __name__ == "__main__":
    doctest.testmod()
    
if __name__ == "__main__":
    unittest.main()