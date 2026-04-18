### **Simulador de Caixa Eletrônico**

#Leia o valor a ser sacado (inteiro, múltiplo de 5, entre 10 e 1000). Calcule a menor quantidade 
# possível de notas de 50, 20, 10 e 5. Exiba a quantidade de cada nota. Caso o valor não esteja 
# dentro das regras, exiba uma mensagem de erro.




valor = int(input("Digite o valor: "))

if valor < 10 or valor > 1000 or valor % 5 != 0:
    print("Valor inválido")
else:
    notas50 = 0
    notas20 = 0
    notas10 = 0
    notas5 = 0

    while valor >= 50:
        valor = valor - 50
        notas50 = notas50 + 1

    while valor >= 20:
        valor = valor - 20
        notas20 = notas20 + 1

    while valor >= 10:
        valor = valor - 10
        notas10 = notas10 + 1

    while valor >= 5:
        valor = valor - 5
        notas5 = notas5 + 1

    print("Notas de 50:", notas50)
    print("Notas de 20:", notas20)
    print("Notas de 10:", notas10)
    print("Notas de 5:", notas5)