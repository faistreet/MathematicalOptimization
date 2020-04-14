import numpy as np

matrix = np.array([[1.,-2.,-3.,0.,0.,0.],[0.,1.,1.,1.,0.,4.],[0.,1.,2.,0.,1.,6.]])
filas=len(matrix)
columnas=len(matrix[0])
cPivote = 0
fPivote = 0

ultColumna = columnas-1
nMenor = matrix[1,ultColumna]
nPivote = 0

sw = 1
while sw == 1:
    mNegativo = 9999
    print ("inicio")
    for f in range(0,filas):
        for c in range(0,columnas):
            if matrix[0,c] < mNegativo:
                mNegativo = matrix[0,c]
                cPivote = c
    
    for p in range(1,filas):
        if matrix[p,ultColumna]/matrix[p,cPivote] < nMenor:
            nMenor = matrix[p,ultColumna] / matrix[p,cPivote]
            fPivote = p
    
    nPivote = matrix[fPivote,cPivote]
              
    for c in range(0,columnas):
        matrix[fPivote,c] = matrix[fPivote,c] / nPivote
    
    for f in range(0,filas):
        factor = matrix[f,cPivote]
        if f != fPivote:
            for c in range(0,columnas):        
                matrix[f,c] = matrix[f,c] - (matrix[fPivote,c] * factor)
    
    for f in range (0,filas):
        print (matrix[f,:])
    
    mNegativo = 0
    for c in range(0,columnas):
        valor = matrix[0,c]
        if  valor < mNegativo:
            mNegativo = valor
            
    if mNegativo < 0:
        sw = 1
    else:
        sw = 0

print("Finalizado.")
