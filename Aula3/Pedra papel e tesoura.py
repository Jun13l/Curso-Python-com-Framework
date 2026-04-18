### **5. Jogo de Pedra, Papel e Tesoura**

#Leia duas jogadas (`"pedra"`, `"papel"` ou `"tesoura"`) e determine o vencedor ou empate. 
# Use condicionais alinhadas.



#Jogo
print('Pedra, Papel e tesoura')
lista_nomes = []
jogador_1 = input('Você: ').lower()
jogador_2 = input('Maquina: ').lower()
lista_nomes.append(jogador_1)
lista_nomes.append(jogador_2)
print('Jogada', lista_nomes)

if jogador_1 == jogador_2:
    print ('Empate')
elif (jogador_1 == 'pedra' and jogador_2 == 'tesoura') or \
     (jogador_1 == 'tesoura' and jogador_2 == 'papel') or \
     (jogador_1 == 'papel' and jogador_2 == 'pedra'):
     print('jogador 1 venceu')
else:
    print('jogador 2 venceu')




