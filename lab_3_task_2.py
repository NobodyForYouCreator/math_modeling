from numpy import pi, tan, cos

h = 100
alfa = pi/3
beta = 30
g = 9.8

V = ((g*h*tan(beta)**2)/2*cos(alfa)**2*(1-tan(beta)*tan(alfa)))**0.5
print(V)

T = 200
Eps = 300
k = 1.38066*10**-23
e = 2.718281828
h = 6.626*10**-12

N = (2/(pi**0.5))*(h/((k*T)**1.5))