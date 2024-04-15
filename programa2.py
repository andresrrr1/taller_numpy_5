#matplotlib tiene muchos modulos 
import numpy as np
import matplotlib.pyplot as plt

#dibujar una funcion seno
#crear un ndarray de 1 dimecion, 100 elementos equiespaciados. de 0 a 2*pi
t=np.linspace(0, 2*np.pi, 100)
x=np.sin(t)
y=np.cos(t)
z=t
#usar matplotlib 
plt.figure(figsize=(8,4))
plt.title('grafico')
plt.xlabel('x')
plt.xlabel('Y')
plt.grid(True)
plt.plot(x,y)
plt.show()


