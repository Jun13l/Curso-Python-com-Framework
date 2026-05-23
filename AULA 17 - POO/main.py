
# framework -  data science
# interface 
# 1 pip install streamlit


# import streamlit as st


# carregar  -  streamli run mome.py




# framework -  data science
# interface 
# 1 pip install streamlit


# import streamlit as st


# carregar  -  streamli run mome.py

import streamlit as st 




# class Portifolio:
#     def __init__(self):
#         nome  =  st.title('Nome')
#         link =  st.error('https://github.com/bea3853')
#         whats = st.write('231321-1231')
#         email =  st.warning('bea@gmail.com')
#         endereco = st.success('rua x, nº x')
#         image = st.image('img.png')
#         audio = st.audio('au.mp3')
#         button =  st.button('Clique aqui')



# ob = Portifolio()
#--------------------------------------

#1
# class Pessoa:
#     pass          # classe vazia

# p = Pessoa()

# ------------------------------------------------------------

#2
# class Carro:
#     rodas = 4                # atributo de classe

#     def __init__(self, modelo):
#         self.modelo = modelo # atributo de instância

#3-----------------------------------------------------------------------------------

# class Exemplo:
#     @classmethod
#     def metodo_classe(cls):
#         print(f"Método de classe:{cls}")

#     @staticmethod
#     def metodo_estatico():
#         print("Método estático")



#4--------------------------------------------------

# class Aluno:
#     def __init__(self, nome, nota):
#         self.nome = nome
#         self.nota = nota



#5-------------------------------------------------------------------------------

# class Calculadora:
#     def somar(self, a, b, c=0):
#         return a + b + c

# calc = Calculadora()
# print(calc.somar(2, 3))      # 5
# print(calc.somar(2, 3, 4))   # 9

# # Sobrecarga de operador
# class Ponto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, outro):
#         return Ponto(self.x + outro.x, self.y + outro.y)