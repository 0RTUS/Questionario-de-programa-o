peso = float(input(""))
altura = float(input(""))

imc = peso / (altura **2)
print(f'{imc:.2f}')

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obeso leve")
elif imc < 40:
    print("Obeso moderado")
elif imc >= 40:
    print("Obeso mórbido")