
from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal

    @abstractmethod
    def tem_cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
        self.cheque_especial = renda_mensal

    def tem_cheque_especial(self):
        return True

class ClienteHomem(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def tem_cheque_especial(self):
        return False

class ContaCorrente:
    def __init__(self):
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f'Depósito: +{valor}')

    def sacar(self, valor, cliente):
        if cliente.tem_cheque_especial() or (self.saldo - valor) >= 0:
            self.saldo -= valor
            self.operacoes.append(f'Saque: -{valor}')
        else:
            print("Saldo insuficiente.")

# Exemplo de uso:
cliente_mulher = ClienteMulher("Mariana", "123456789", 10000)
cliente_homem = ClienteHomem("Pedro", "987654321", 5000)

conta_mariana = ContaCorrente()
conta_Pedro = ContaCorrente()

conta_mariana.depositar(2000)
conta_mariana.sacar(6000, cliente_mulher)  # Saque com cheque especial
conta_mariana.sacar(6000, cliente_mulher)  # Tentativa de saque sem saldo suficiente

conta_Pedro.depositar(1500)
conta_Pedro.sacar(4000, cliente_homem)  # Tentativa de saque sem cheque especial

print(f"Saldo conta Mariana: {conta_mariana.saldo}")
print(f"Operações conta Mariana: {conta_mariana.operacoes}")

print(f"Saldo conta Pedro: {conta_Pedro.saldo}")
print(f"Operações conta Pedro: {conta_Pedro.operacoes}")

