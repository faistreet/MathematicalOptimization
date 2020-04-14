import numpy as np
matriz=np.array([[2,6,1],
                 [1,2,-1],
                 [5,7,-4]], dtype=np.float64)

vector=np.array([7,-1,9], dtype=np.float64)

filas=matriz.shape[0]
columnas=matriz.shape[1]

x=np.zeros((filas))

for k in range(0,filas):
    for r in range(k+1,filas):
        factor=(matriz[r,k]/matriz[k,k])
        vector[r]=vector[r]-(factor*vector[k])
        for c in range(0,columnas):
            matriz[r,c]=matriz[r,c]-(factor*matriz[k,c])        
    
    x[filas-1]=vector[filas-1]/matriz[filas-1, filas-1]
    
for z in range (filas-1, 0, -1):
        for x in range (z):
            if (matriz[z][z] != 0):
                p = matriz[x][z] / matriz[z][z]
                matriz[x][z] = matriz [x][z] - (matriz[z][z] * p)
                vector[x] = vector[x] - (vector[z] * p)
                
       

print('Resultado matrix')        
print(matriz)
print('vector')
print(vector)
