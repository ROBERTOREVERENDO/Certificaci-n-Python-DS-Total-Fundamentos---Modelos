import unittest

def POTENCIA (BAS,POT):
    return BAS ** POT

def ES_PAR (NUM):
    if NUM % 2 == 0:
        return True
    else:
        return False
    
def INVERTIR_CADENA (CADENA):
    return CADENA[::-1]

class PRUEBA_UNITARIA(unittest.TestCase):
    def test_POTENCIA(self):
        self.assertEqual(POTENCIA (4,3),64)
        self.assertFalse(POTENCIA (4,3) == 63)
        
        VARIABLE = None
        self.assertIsNone(VARIABLE)
        
      
    def test_ES_PAR(self):
        self.assertNotEqual(ES_PAR(5),True)
        self.assertNotEqual(ES_PAR(4),False)
        self.assertIs(ES_PAR(5),False)
        self.assertIs(ES_PAR(4),True)
        
        VARIABLE = not(None)
        self.assertIsNotNone(VARIABLE)
        
        
    def test_INVERTIR_CADENA(self):
        self.assertTrue(INVERTIR_CADENA("XYZ") == "ZYX")
        self.assertIsNot(INVERTIR_CADENA("XYZ"),"XYZ")
        self.assertIn(INVERTIR_CADENA("XYZ"),["ABC","ZYX"])
        self.assertNotIn(INVERTIR_CADENA("XYZ"),["ABC","DEF"])
  
if __name__ == "__main__":
    unittest.main()
    
