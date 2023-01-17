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
    
    >>> A = 3
    >>> B = 2
    >>> POTENCIA (A,B)
    9
    
    >>> A = 0
    >>> for X in range(3):
    ...     A = A + X
    >>> B = 1
    >>> for X in range(4):
    ...     if X % 2 == 0:
    ...         B = B + X
    >>> POTENCIA (A,B)
    27
    
    """
    return BAS ** POT

if __name__ == "__main__":
    import doctest
    doctest.testmod()