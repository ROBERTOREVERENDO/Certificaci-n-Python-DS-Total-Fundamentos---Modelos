#MÉTODO 1 DE INVOCACIÓN
import CARPETA.SCRIPT_PRUEBA
CARPETA.SCRIPT_PRUEBA.FUNCION_PRUEBA()
CARPETA.SCRIPT_PRUEBA.FUNCION_PRUEBA2()

# #MÉTODO 2 DE INVOCACIÓN
from CARPETA.SCRIPT_PRUEBA import *
FUNCION_PRUEBA()
FUNCION_PRUEBA2()

# #MÉTODO 3 DE INVOCACIÓN
from CARPETA.SCRIPT_PRUEBA import FUNCION_PRUEBA
FUNCION_PRUEBA()
#FUNCION_PRUEBA2()
