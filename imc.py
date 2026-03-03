def calcula_imc (peso, altura_cm):
    altura_m = altura_cm / 100 #converte cm para m
    return peso / (altura_m ** 2)

peso = eval(input("Qual o seu peso em Kg? "))
altura = eval(input("Qual a sua altura em cm? "))
calcula_imc(peso, altura)
imc = calcula_imc(peso, altura)

print (f"imc = {imc: .2f}")

if imc < 18.5:
    print ("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print ("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print ("Sobrepeso")
elif imc >= 30 and imc <= 39.9:
    print ("Obesidade")
else:
    print ("Obesidade grau III")