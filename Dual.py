import numpy as np

matrix = np.array([[1.,-30.,-50.,0.,0.,0.],[0.,-10.,-15.,1.,0.,-40.],[0.,-12.,-20.,0.,1.,-40.]])
filas=len(matrix)
columnas=len(matrix[0])
cValor = columnas-1
nMenor = 999999
cPivote = 0
fPivote = 0

for f in range(1,filas):
    for c in range(1,3):
        valor = matrix[f,cValor] / matrix[f,c]
        if valor < nMenor:
            nMenor = valor
            cPivote = c
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

print (fPivote)