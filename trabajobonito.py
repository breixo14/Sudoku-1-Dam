


def numerosEnRango(sudoku):

    if sudoku==[]:
        return False

    for fila in sudoku:
        for i in fila:
            if not isinstance(i,(int)):
                return False

    return True




def checkCuadrado(sudoku):
    
    
    largo=len(sudoku)
    ancho=len(min(sudoku))

    if largo==ancho:
        return True
    return False





def checkFilas(sudoku):
    
    lista=list(range(1, len(sudoku)+1)) 
    for i in sudoku:
        if sorted(i)!=lista: 
            return False
    return True




def checkColumnas(sudoku):

    
    assert isinstance(
        sudoku, list), "la interfaz exige que sudoku debe ser una lista"

    lista=list(range(1, len(sudoku)+1))
    comparacion=[]
    comparacion2=[]
    valor=0
    contador=-1
    largo=len(sudoku)

    while True:
        contador+=1
        if contador==largo:
            break
        for elemento in sudoku:
            comparacion2=list(elemento)
            comparacion.append(comparacion2[contador])
        if sorted(comparacion)!=lista:
            return False
        comparacion=[]
    return True

