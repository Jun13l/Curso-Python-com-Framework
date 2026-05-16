
#4 Atividade 15

# class Calculadora:


#     @staticmethod
#     def soma(a,b):
#         return a + b
    
#     @staticmethod
#     def subtrair(a,b):
#         return a - b


#     @staticmethod
#     def mult(a,b):
#         return a * b
    
#     @staticmethod
#     def div(a,b):
#         return a / b
    
# print(Calculadora.mult(100,200))

#---------------------------------------------------------------
#5 EQ- EQUIVALENTES
# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca =  marca
#         self.modelo = modelo
#         self.ano  =  ano


#     def __eq__(self, outro):
#         return(
          
#         self.marca == outro.marca and 
#         self.modelo == outro.modelo and 
#         self.ano == outro.ano


#         ) 
        
        
# c1  =  Carro('ford','fiesta','2024')
# c2  =  Carro('Volks','fusca','2020')
# c3  =  Carro('ford','fiesta','2024')



# print(c1 == c3)


# print(c2 == c1)

#--------------------------------------------------------------------------
#9__len__


# class Funcionario:
#     def __init__(self, nome, cargo, salario):
#         self.nome =  nome
#         self.cargo = cargo
#         self.salario = salario




#     def __len__(self):
#         return len(self.nome)
    



# f  =  Funcionario('diogo', 'dev', '5000')
# print(f.__len__())    


#______________________________________________________________________________________





    