#MÉTODO 1 DE INVOCACIÓN
import SCRIPT_PRUEBA
SCRIPT_PRUEBA.FUNCION_PRUEBA()
SCRIPT_PRUEBA.FUNCION_PRUEBA2()

#MÉTODO 2 DE INVOCACIÓN
from SCRIPT_PRUEBA import *
FUNCION_PRUEBA()
FUNCION_PRUEBA2()

#MÉTODO 3 DE INVOCACIÓN
from SCRIPT_PRUEBA import FUNCION_PRUEBA
FUNCION_PRUEBA()
FUNCION_PRUEBA2()


