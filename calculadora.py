#Obesidad: Más de 30.0
#Peso inferior al normal: Menos de 18
#Peso superior al normal: 26 – 29
#Normal: 19 – 25

def calcularIMC() :
    print("calcularIMC1")

calcularIMC()

def pedirPeso() :
    peso = int(input("ingrese su peso en kg"))
    alturaEnCm = int(input("ingrese su altura en cm"))
    alturaEnM = alturaEnCm /100


    imc = peso / (alturaEnM * alturaEnM)

    if imc <= 18 :
            print("Peso inferior al normal")

    if imc >= 19 and imc <= 25 :
            print("Normal")

    if imc >= 26 and imc <=29 : 
            print("Peso superior al normal")

    if imc >= 30 :
            print("Obesidad")
    print("su IMC es de " + str(imc))
print("calcular el IMC de la primer persona")
pedirPeso()
print("calcular el IMC de la segunda persona")
pedirPeso()                
print("calcular el IMC de la tercera persona")
pedirPeso()