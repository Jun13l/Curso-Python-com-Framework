### **Imposto de Renda Simplificado**

#Leia o salário bruto mensal e calcule o desconto do INSS (11% sobre o salário, limitado a R$ 1.500,00) 
# e o IRRF conforme tabela:

#- Isento se salário bruto ≤ R$ 2.500,00
#- 7,5% sobre o que exceder R$ 2.500,00 até R$ 3.500,00
#- 15% sobre o que exceder R$ 3.500,00 até R$ 5.000,00
#- 27,5% sobre o que exceder R$ 5.000,00
#Exiba o salário líquido após os descontos.

#salario


salario = float(input('R$: '))
inss = salario * 0.11
(print('Desconto Inss:', inss))
salario = salario - inss
if salario >= 1500.0 and salario <= 2500.0:
    print('desconto do salario', salario)

#Inss

if inss > 1500:
    inss = 1500


base = salario - inss




#IR
if base <= 2500:
    ir = 0
elif base <= 3500:
    ir = base * 0.075
elif base <= 5000:
    ir = base * 0.15
else:
    ir = base * 0.275

salario_liquido = salario - inss - ir
print('Salário Liquido', salario_liquido)




