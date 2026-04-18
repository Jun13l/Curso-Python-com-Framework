### **Validação de Triângulo**

#Leia três lados de um triângulo. Verifique se eles formam um triângulo (cada lado é menor que a soma dos outros dois). Se sim, classifique como:

#- `"Equilátero"` (todos os lados iguais)
#- `"Isósceles"` (dois lados iguais)
#- `"Escaleno"` (todos diferentes)

a = [float(input('lado1: '))]
b = [float(input('lado2: '))]
c = [float(input('lado3: '))]



#Classificação
if a < b + c and b < a + c and c < b + a:
   if a == b == c:
    print('Equilátero')
   elif a == b or b == c or c == a:
    print('Isóceles')
else:
    print('Escaleno')

    print('Não Forma triangulo')

