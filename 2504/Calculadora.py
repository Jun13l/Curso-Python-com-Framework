def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "erro: divisão por zero"
    return a / b


# programa principal
while True:
    print("\n--- Calculadora ---")

    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))

    op = input("Operação (+, -, *, /) ou 'sair': ")

    if op == "sair":
        print("Encerrando...")
        break

    if op == "+":
        print("Resultado:", somar(n1, n2))

    elif op == "-":
        print("Resultado:", subtrair(n1, n2))

    elif op == "*":
        print("Resultado:", multiplicar(n1, n2))

    elif op == "/":
        print("Resultado:", dividir(n1, n2))

    else:
        print("Operação inválida")
