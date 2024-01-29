# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
# Crie uma instância da classe carro.
# Faça o carro "andar" utilizando os métodos da sua classe.
# Faça o carro "parar" utilizando os métodos da sua classe.

class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0

    def liga(self):
        if not self.ligado:
            print("O carro está ligado.")
            self.ligado = True
        else:
            print("O carro já está ligado.")

    def desliga(self):
        if self.ligado:
            print("O carro está desligado.")
            self.ligado = False
            self.velocidade = 0
        else:
            print("O carro já está desligado.")

    def acelera(self, incremento):
        if self.ligado:
            self.velocidade += incremento
            print(f"O carro acelerou e está a {self.velocidade} km/h.")
        else:
            print("O carro precisa estar ligado para acelerar.")

    def desacelera(self, decremento):
        if self.ligado and self.velocidade >= decremento:
            self.velocidade -= decremento
            print(f"O carro desacelerou e está a {self.velocidade} km/h.")
        elif self.ligado and self.velocidade < decremento:
            self.velocidade = 0
            print("O carro parou.")
        elif self.ligado and self.velocidade == 0:
            print("O carro já está parado.")
        else:
            print("O carro precisa estar ligado para desacelerar.")

    def __str__(self):
        return f"Carro {self.modelo}, cor {self.cor}, velocidade {self.velocidade} km/h"


# Criando uma instância da classe Carro
meu_carro = Carro(cor="Azul", modelo="Sedan")

# Exibindo a representação do carro
print(meu_carro)

# Ligando o carro
meu_carro.liga()

# Acelerando o carro
meu_carro.acelera(30)

# Desacelerando o carro
meu_carro.desacelera(10)

# Parando o carro
meu_carro.desacelera(20)

# Exibindo a representação do carro
print(meu_carro)

# Desligando o carro
meu_carro.desliga()

