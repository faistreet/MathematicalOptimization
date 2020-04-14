import numpy as np

matrix = np.array([[1.,-5000.,-6000.,-3000.,0.,0.,0.,0.],[0.,5.,3.,2.,1.,0.,0.,150.],[0.,3.,4.,3.,0.,1.,0.,120],[0.,4.,5.,1.,0.,0.,1.,200.]])
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

    for c in range(0,columnas):
        if matrix[0,c] < mNegativo:
            mNegativo = matrix[0,c]
            cPivote = c

    
    for f in range(1,filas):
        if matrix[f,ultColumna]/matrix[f,cPivote] < nMenor:
            nMenor = matrix[f,ultColumna] / matrix[f,cPivote]
            fPivote = f
    
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