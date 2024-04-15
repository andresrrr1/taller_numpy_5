#taller: calculos numericos en arreglos n dimencionales 
#narray de 2 dimeciones a partir de la lista 
import numpy as np
import matplotlib as plt

a=np.array([[1,5],[7,9]])
b=np.array([[2,0],[1,3]])


#producto 
c=np.dot(a,b)
#solucion de un sistema de ecuaciones con numpy 
solucion=np.array([5,17])

m=np.linalg.solve(a,solucion)
print(m)

