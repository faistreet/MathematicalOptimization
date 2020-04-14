def formula(x,fx):
    b0=fx[0]
    b1=(fx[1]-fx[0])/(x[1]-x[0])
    b2=((fx[2]-fx[1])/(x[2]-x[1])-((fx[1]-fx[0])/(x[1]-x[0])))/(x[2]-x[0])
    f2=b0+b1*(x[3]-x[0])+b2*(x[3]-x[0])*(x[3]-x[1])
    return(f2)
     
x=[1,2,3]
fx=[3,-5,6]

vx=float(input("introduce el valor de x para calcular f(x): "))
x.append(vx)        
print("El valor de f(x) es:", formula(x,fx))