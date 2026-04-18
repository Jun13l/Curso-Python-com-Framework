### **Validação de Data**

#Leia um dia (1-31), mês (1-12) e ano (qualquer). Verifique se a data é válida, considerando meses com 30/31 dias e fevereiro (28 ou 29 dias, considerando ano bissexto: divisível por 400 ou (divisível por 4 e não por 100)).






dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# Verifica se o mês é válido
if mes < 1 or mes > 12:
    print("Data inválida")
else:
    # Descobrir se é ano bissexto
    bissexto = False
    if ano % 400 == 0:
        bissexto = True
    elif ano % 4 == 0 and ano % 100 != 0:
        bissexto = True

    # Definir dias do mês
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        max_dias = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        max_dias = 30
    else:  # fevereiro
        if bissexto:
            max_dias = 29
        else:
            max_dias = 28

    # Verificar dia
    if dia >= 1 and dia <= max_dias:
        print("Data válida")
    else:
        print("Data inválida")