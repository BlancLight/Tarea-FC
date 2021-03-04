# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 18:33:59 2021
Codigo del metodo de Newton-Cotes de Trapecio para la aproximar la solucion del desplazamiento de un objeto
@author: acraw
"""

#Tiempo inicial
a=0
#Tiempo final
b=100
#Numero de intervalos para realizar el calculo
N=100
h=(b-a)/(N-1)
#Velocidad inicial 
Vi=float(0.5)
#Velocidad final
Vf=float(1.0)
#Aceleracion
aceleracion=(Vf-Vi)/b
#Valor inicial de la suma del metodo a realizar
Sumatoria=0

#Definos la funcion de peso que va a multplicar a los valores de la funcion evaluados en cada ti
def PesoWi(i,h):
    if ((i==1) or (i==N)): wi = h/2.0
    else: wi = h
    return wi
#Definimos la funcion V(t) que se utilizara para realizar la aproximacion
def V(t):
    return Vi+aceleracion*t

#Este for va a realizar la suma de todos las areas calculadas mas las correcciones del peso
for i in range(1,N+1):
        ti=a+(i-1)*h
        peso=PesoWi(i, h)
        Sumatoria=V(ti)*peso+Sumatoria
#Se calcula el procentaje de error entre el valor aproximado y el valor exacto
ValorExacto=75
Error=((Sumatoria-ValorExacto)/ValorExacto)*100
    
#Se imprime el resultado obtenido
print('La aproximacion es',Sumatoria,'con un error de',Error,'porciento')
    
    