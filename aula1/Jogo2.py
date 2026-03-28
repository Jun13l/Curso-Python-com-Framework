# Pergunta: Qual e o metal cujo símbolo químico é Au?
# Pergunta: Em qual continente fica o Deserto do Saara?
# Resposta: No continente Africano.
# Pergunta: Quem é o autor da obra "Dom Quixote"?
# Resposta: Miguel de Cervantes.
# Pergunta: Qual é o processo pelo qual as plantas transformam luz solar em energia química?
# Resposta: Fotossíntese.


# jogo de advinhação
import random  


# lista_pc  = ['😘','👍','🤣','😒']
# # nossa_lista = ['😘','👍','🤣']
# aleatorio = random.choice(lista_pc)
# escolha_personagem = input('teste: ')
# resultado = aleatorio == escolha_personagem


# print('ACERTOU? - ', resultado)
# print('ESCOLHA DA MAQUINA: ', aleatorio)
# print('MINHA ESCOLHA:', escolha_personagem)




# Pergunta: Qual é o metal cujo símbolo químico é Au?


# Resposta: Ouro. O símbolo vem do latim aurum.


# Pergunta: Em qual continente fica o Deserto do Saara?


# Resposta: No continente Africano.


# Pergunta: Quem é o autor da obra "Dom Quixote"?


# Resposta: Miguel de Cervantes.


# Pergunta: Qual é o processo pelo qual as plantas transformam luz solar em energia química?


# Resposta: Fotossíntese.


listas_perguntas = [
'',    
'Qual é o metal cujo símbolo químico é Au?',
'Em qual continente fica o Deserto do Saara?',
'Quem é o autor da obra "Dom Quixote"?',
'Qual é o processo pelo qual as plantas transformam luz solar em energia química?'
]


pergunta =  random.choice(listas_perguntas[1])
print(pergunta)

print(lista_respostas[1])
resposta = int(input('ESCOLHA UM NUMERO - (1) (2) (3) (4)'))

1 = lista_perguntas,index(pergunta)
pontos = 0
resultado = (resposta == 1) + pontos


print ('Resultado acertou ? ', resposta == 1)
print ('Pontuação', resultado)