# -*- coding: utf-8 -*-
"""
El presente codigo se encarga de tomar una funcion x(t) y hallar la raiz de esa funcion.
"""
#La biblioteca sympy permite realizar calculos en forma simbolica
import sympy as sym

#t va a ser la variable tiempo en segundos
t = sym.symbols('t')
#t0 es el tiempo inicial
t0 = 4
#x0 es la posicion inicial
x0 = -5.00
#v0 es la velocidad inicial
v0 = 0
#a es la aceleracion constante que tiene la particula
a = 0.01
#N es la cantidad de iteraciones a utilizar
N = 5
#i es un contador
i = 0
#Tol es la tolerancia del error que se quiere alcanzar
Tol = 0.01
#x(t) es la funcion de desplazamiento en el eje x.
funcion_posicion = x0 + v0*t + 0.5*a*t*t
#Como v0 = 0 se puede despejar el tiempo t a una posicion de x = 0.0
#De esto se obtiene que t = 31.6227766s
#Por esto el valor exacto es:
v_exacto = 31.6227766

#Esta funcion calcula la derivada de x(t) en forma simbolica
def Derivada_x(x,t):
    der = sym.diff(x,t)
    return der

#Esta es la funcion principal que aplica el metodo de NewtonRaphson para encontrar la raiz de la funcion
#Esta retorna una lista que alberga las aproximaciones ti, la cantidad de iteraciones y el error relativo
def NewtonRaphson(i,N,t,funcion_posicion,t0,Tol,v_exacto):
    ErrorRela = 100000 #Error relativo, este se fija en un valor grande para que siempre suceda el ciclo.
    while i < N and Tol < ErrorRela: 
        i = i + 1
        x_t0 = funcion_posicion.subs(t,t0)
        derivada = Derivada_x(funcion_posicion,t)
        valor_derivada = derivada.subs(t,t0)
        ti = t0 - x_t0/valor_derivada #Formula de Newton Raphson
        ErrorRela = (abs(ti-v_exacto)/v_exacto)*100 #Error relativo con el valor exacto en porcentaje
        t0 = ti
    list1 = [ti,N,ErrorRela] #Esta lista va a albergar la aproximacion mas reciente en la primer columna, en la segunda columna tiene la cantidad de iteraciones, en la tercera el error relativo con el valor exacto.
    return list1 #Los valores ti van a ser las aproximaciones consecutivas 

list2 = ["Aproximacion","Cantidad de iteraciones","Error relativo %"]
print(list2)
print(NewtonRaphson(i,N,t,funcion_posicion,t0,Tol,v_exacto))



