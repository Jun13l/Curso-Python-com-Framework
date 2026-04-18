idade = int(input("idade: "))
plano = input("Digite o plano (basico, standard, premium): ")

valor = 0

if plano == "basico":
    valor = 100 + (idade * 2)
elif plano == "standard":
    valor = 150 + (idade * 3)
elif plano == "premium":
    valor = 200 + (idade * 5)
else:
    print("Plano inválido")

# acréscimo para maiores de 60
if idade > 60:
    valor = valor + (valor * 0.10)

print("Valor mensal: R$", valor)