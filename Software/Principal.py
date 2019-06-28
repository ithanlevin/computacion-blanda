from LogicaDifusa import *
from Backpropagation import *
from SistemaExperto import *


A = input("Ingrese El Estado De La Carretera :     -")
B = input("Ingrese La Hora Del Dia:     -")
C = input("Ingrese La Intensidad De Lluvia:   -")
D = input("Ingrese El Dia De La Semana:    -")
E = input("Ingrese El Mes Del Anio:   ")

riesgo = CalcularRiesgo(A,C,B,D,E)

e=Binario(riesgo)
d=[0,0,0,0]
entrada=[[[e[0],e[1],e[2],e[3],e[4],e[5],e[6],d[0],d[1],d[2],d[3]],[0,0]]]
accidentalidad=0
output =red.Resultado(entrada)

if output[0]==0 and output[1]==0:
    accidentalidad=0
elif output[0]==0 and output[1]==1:
    accidentalidad=1
elif output[0]==1 and output[1]==0:
    accidentalidad=2
elif output[0]==1 and output[1]==1:
    accidentalidad=3

V(accidentalidad,Velocidad_Sugerida)
print "Velocidad Sugerida:",Velocidad_Sugerida.v(),"km/h"
