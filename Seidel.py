import numpy

x=numpy.zeros((3))
matrix=numpy.array([[9,2,-1],[7,8,5],[3,4,-10]])
vector=numpy.array([-2,3,6])
filas=matrix.shape[0]
columnas=matrix.shape[1]
comprobacion=numpy.zeros((filas))
error=[]

tolerancia=float(input("¿Cual es la toletancia al error?"))
iteraciones=int(input("¿Cual es el numero de iteraciones"))
k=0

while k<iteraciones:
        suma=0
        k=k+1
        for r in range(0,filas):
            suma=0
            for c in range(0,columnas):
                if (c != r):
                    suma=suma+matrix[r,c]*x[c]
                x[r]=(vector[r]-suma)/matrix[r,r]
            print("x["+str(r)+"]: "+str(x[r]))
        del error[:]
        
        for r in range(0,filas):
            suma=0
            for c in range(0,columnas):
                suma=suma+matrix[r,c]*x[c]
            comprobacion[r]=suma
            diferencia =abs(comprobacion[r]-vector[r])
            error.append(diferencia)
            print("Error en x[",r,"]=",error[r])    
        print("Iteraciones",k)
        if all( i<=tolerancia for i in error)==True:
            break