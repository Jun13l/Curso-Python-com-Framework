### **Cálculo de IMC com Faixas**

#Leia peso (kg) e altura (m). Calcule o IMC e classifique conforme a tabela da OMS:

#- `"Abaixo do peso"` se IMC < 18.5
#- `"Peso normal"` se 18.5 ≤ IMC < 25
#- `"Sobrepeso"` se 25 ≤ IMC < 30
#- `"Obesidade"` se IMC ≥ 30

peso = float(input('Digite seu Peso: '))
altura = float(input('Digite sua Altura: '))
imc = peso / altura ** 2

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >18.5 and imc <25:
    print('Peso Normal')
elif imc >=25 and 30:
    print('Sobrepeso')
else:
    print('Obesidade')