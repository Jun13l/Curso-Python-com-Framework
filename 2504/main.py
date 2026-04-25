# #for = loop finito
# #while true = loop infinito

# # while = enquanto

# # for i in range(10):
# #     print(i)
# #             # start stop step by step


# # estrturas compostas


# # n =  10
# # x  =  5.9
# # x =  'True'


# # variavel_texto = 'isso é um texto'
# # lista = [1,0,2,3,6]
# # dicionario = {
# #     'a':10,
# #     'b':20
# #     }
# # c =  {1,2,3,6}
# # tupla = (5,6,6,5)


# # for i in range(15):
# #     nome  =  input('nome: ')
# #     
#             # start stop step by step
           
# #for i in lista:
#  #   print(i)


# # for i in variavel_texto:
# #     print(i)
            
# # for x, y in dicionario.items():
# #     print(x, y)
# # 
# # for i in  tupla:
# #     print(i)
 
# # for z  in x:
# #     print(z)


# # --------------------------------------


# # while True:
# # #     print('teste')
# # import time


# # contador = 0  
# # while contador <= 10:
# #     print(contador)
# #     time.sleep(2)
# #     contador =  contador + 1
    


# # pergunta = input('Deseja adicionar um dado a lista? ')
# # lista = []
# # while pergunta == 'sim':
# #       nome = input('nome: ')
# #       lista.append(nome)
# #       pergunta = input('deseja continuar? ')
# #       print(lista)

# #Tabuada

# # n =  int(input('numero: '))

# # import time
# # for x in range(1,11):
# #    c = x * n
# #    print(n , 'x', x , '=', c )



# # Ex: tabuada


# # import time
# # numero =  int(input('numero inteiro: '))
# # for x in range(11):
# #     r =  numero * x
# #     print(numero, 'x', x , '=', r)
# #     time.sleep(2)

# #### **2. Contagem Regressiva com Pausa**



# #Peça um número inteiro positivo. Use `while` para fazer uma contagem 
# # regressiva até 0, exibindo cada número. Após o término, exiba `"Fogo!"`


# # import time
# # n = int(input('Digite numero inteiro: '))

# # while n >= 0:
# #   print(n)
# #   n -= 1


# ### **3. Média de Notas com `while`**

# # Peça notas até que o usuário digite `-1`. Calcule e exiba a média das notas válidas (0 a 10). Ignore entradas inválidas e use `continue` quando necessário.

# # soma = 0
# # cont = 0

# # while True:
# #     n = float(input('Digite sua nota: '))
# #     if n == -1:
# #         break
# #     if n < 0 or 10> n:
# #         continue

# #     soma = soma + n
# #     cont = cont + 1

# #     if cont != 0:
# #         print(soma / cont)
# # else:
# #     print('Sem notas Válidas')
# # _______________________________


# ### **4. Validação de Senha com Limite de Tentativas**

# # Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. Se acertar, exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.



# senha_certa = '031295'
# tent = 0

# while tent < 3:
#     s = input('Digite Sua senha: ')
#     if s == senha_certa:
#         print('Acesso liberado')
#         break
        
#         tent = tent + 1
        
        
#         if tent == 3:
#             print('Acesso bloqueado')








