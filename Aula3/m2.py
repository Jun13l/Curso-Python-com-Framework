idade =  int(input('Idade: '))
carta_m =  input('POssui carta sim ou não?')
decisao =  idade>=18 and carta_m == 'sim' and 'Pode dirigir' or 'não pode...'
print(decisao)

#IF = SE
if idade >= 18 and carta_m == 'sim':
    print('Pode ')
#ELSE = SE NÃO

else:
    print('Não pode')
    
if idade >= 18:
   if carta_m == 'sim':
       print('Pode ')
else:
    print('Não pode')
    
    
if idade >= 18 and carta_m == 'sim':
   print('Pode ')
#Elif = Elife é uma terceira opção
elif idade >= 18 and carta_m == 'não':
   print('pode tirar a carta')
else:
   print('Não pode')
