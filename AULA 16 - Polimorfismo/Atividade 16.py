class Animal:
    def falar(self):
        print("O animal faz um som")

class Cachorro(Animal):

    def falar(self):
        print("O cachorro late")

class Gato(Animal):
    def falar(self):
        print("O gato mia")

a1 = Cachorro()
a2 = Gato()

a1.falar()
a2.falar()