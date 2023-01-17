import sys

#RECOMENDACIÓN MUY IMPORTANTE
#DEBES VALIDAR QUE TE PROVEAN LA CANTIDAD DE PARÁMETROS CORRECTA

#python SCRIPT.py 12 15 16 19

#sys.argv[0]  --> NO LO PUEDES UTILIZAR
#sys.argv[1]  --> PRIMER PARÁMETRO
#sys.argv[2]  --> SEGUNDO PARÁMETRO
#sys.argv[3]  --> TERCER PARÁMETRO
#sys.argv[4]  --> CUARTO PARÁMETRO

#VALIDACIÓN PARA OBTENER CANTIDAD DE PARÁMETROS CORRECTO
# len(sys.argv) == PARAMETROS + 1

#LOS PARÁMETROS SE PASAN BY DEFAULT EN CADENA
#DEBES MODIFICARLOS

def SUMA(A,B,C,D):
    return A+B+C+D

if len(sys.argv) == 4 + 1:
    print(SUMA( int(sys.argv[1]) , int(sys.argv[2]) , int(sys.argv[3]) , int(sys.argv[4])))
else:
    print("ERROR EN LA CANTIDAD DE PARÁMETROS PROVISTOS")