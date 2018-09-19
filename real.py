y=[4,15,24,56]
print"El primero es",y[0],"ultimo",y[3]

print range(7)

for i in range(3):
    print "hola"
    print "rodrigo guay"
print "hasta pŕonto"

y.append("bye")
print y


x=[100]
for i in range(10):
    x.append(1.01*x[i])
print x


x=[1,1]
for i in range(15):
    x.append(x[i]+x[i+1])
print x

import matplotlib.pyplot as plt

plt.plot(x)
plt.show(x)


def suma(x,y):
    return x+y


suma(2,3)

def producto(r,s):
    return r*s

producto(5,6)

def operacion(x,y,f):
    return f(x,y)

operacion(6,5,producto)


def r(x):
    return 1.01*x

def ru(x_0,iteraciones,r):
    x=[x_0]
    for i in range(iteraciones):
        x.append(r(x[i]))
    return x

ru(5,100,10)



import math
ru(1000000000000000000000000000000000000000000000000000000000010,30,math.cos)
    

import numpy as np

def diagrama(f, x0, it):
    x= [x0]
    y= [x0]
    s= np.arange(0,1, 0.01)
    for i in range(it):
        x.append(x[2*i])
        x.append(f(x[2*i]))
        y.append(f(y[2*i]))
        y.append(f(y[2*i]))
    plt.plot(x,y,color='red')
    plt.plot(s,f(s))
    plt.plot(s,s,color='black')
    plt.show


def logistica(x):
    
     return 2*x*(1-x)
     
diagrama(logistica,0.1,100)

