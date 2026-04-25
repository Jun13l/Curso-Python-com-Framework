# # ### **7. Soma de Dígitos**

# # Peça um número inteiro positivo e calcule a soma de seus dígitos.
# # Use `while` para extrair os dígitos um a um.


# # import time
# # n = int(input('Digite seu Numero: '))
# # soma = 0

# # while n >= 0:
# #     d = n % 10
# #     soma = soma + n
# #     n + n // 10
# #     print(soma)



# ### **8 Menu Interativo**

# Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. As opções podem ser:

# - `1` – Exibir mensagem "Olá!"
# - `2` – Exibir a data/hora atual (use `import datetime`)
# - `3` – Sair

# Use `while True` e `break` para sair



# i  =  input('digite o numero')
# c = 0
# while c <=0:
#     z   =  [int(x) for x  in i]
#     s = sum(z)
#     c  =  c + 1
# print(s) 

x  =  input('digite um numero: ') 
l = []
n = 0
while n < len(x):
    #   print(n)
      l.append(int(x[n]))
      n += 1



print(l)
print(sum(l))