class Aviao():

    def __init__ (self, marca, modelo, peso):

        self.marca = marca
        self.modelo = modelo
        self.peso = peso

    def decolar(self):
        print("O Avião está decolando")

    def pousar(self):
        print("O Avião está pousando")