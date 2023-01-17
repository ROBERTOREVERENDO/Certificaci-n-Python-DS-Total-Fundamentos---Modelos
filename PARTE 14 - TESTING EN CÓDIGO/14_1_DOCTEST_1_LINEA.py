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
    
    >>> POTENCIA (4,2)
    16
    
    >>> POTENCIA (4,-1)
    0.25
    
    >>> POTENCIA (4,0.5)
    2.0
    
    >>> POTENCIA (4,0)
    1
    """
    return BAS ** POT

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#print(POTENCIA (4,2))
#print(POTENCIA (4,-1))
#print(POTENCIA (4,0.5))
#print(POTENCIA (4,0))