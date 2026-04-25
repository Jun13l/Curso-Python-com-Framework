# ### **1. Calculadora com Funções**

# # Crie funções separadas para as quatro operações básicas (`somar`, `subtrair`, `multiplicar`, `dividir`). Em seguida, escreva um programa que leia dois números e a operação desejada (como string) e chame a função correspondente.
# #  A divisão deve tratar divisão por zero.

# #Somar
# #Subtrair
# #Multiplicar
# #dividir

# ### **1. Calculadora com Funções**

# #Crie funções separadas para as quatro operações básicas (`somar`, `subtrair`, `multiplicar`, `dividir`). 
# #Em seguida, escreva um programa que leia dois números e a operação desejada (como string) e chame a função correspondente. A divisão deve tratar divisão por zero.



# # def somar(a, b):
# #     return a + b

# # def subtrair(a, b):
# #     return a - b

# # def multiplicar(a, b):
# #     return a * b

# # def dividir(a, b):
# #     if b == 0:
# #         return "erro: divisão por zero"
# #     return a / b



# # while True:
# #     print("\n--- Calculadora ---")

# #     n1 = float(input("Primeiro número: "))
# #     n2 = float(input("Segundo número: "))

# #     op = input("Operação (+, -, *, /) ou 'sair': ")

# #     if op == "sair":
# #         print("Encerrando...")
# #         break

# #     if op == "+":
# #         print("Resultado:", somar(n1, n2))

# #     elif op == "-":
# #         print("Resultado:", subtrair(n1, n2))

# #     elif op == "*":
# #         print("Resultado:", multiplicar(n1, n2))

# #     elif op == "/":
# #         print("Resultado:", dividir(n1, n2))

# #     else:
# #         print("Operação inválida")


# # =======================================================================================================
# # =======================================================================================================
# # =======================================================================================================


# ### **2. Validador de CPF (simplificado)**

# Crie uma função `validar_cpf(cpf)` que recebe uma string com 11 dígitos e retorna `True` se for válido (use o algoritmo básico de validação de CPF). Em seguida, teste a função com alguns CPFs.





# def verificar_cpf(cpf):
#     if len(cpf) != 11:
#         print('digite algo válido...')
#     else:
#         soma = 0
#         for x in range(9):
#             soma  = soma +  int(cpf[x]) * ( 10 - x)


#         if soma == 10:
#            soma = 1      
        
#         print((soma *10 ) % 11)
#         soma1 = 0
#         for x in range(10):
#             soma1  = soma1 +  int(cpf[x]) * ( 11 - x) 
#         if soma1 == 10:
#            soma1 = 1     
#         print((soma1 *10 ) % 11)
        


# verificar_cpf('57974208058')            

# ==========================================================================================================
# ==========================================================================================================


### **3. Gerador de Tabuada**

# Escreva uma função `tabuada(numero, inicio=1, fim=10)` que exibe a tabuada do `numero` no intervalo `[inicio, fim]`. 
# Se os argumentos `inicio` e `fim` não forem fornecidos, use 1 e 10.


