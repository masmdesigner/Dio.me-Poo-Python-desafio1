from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

# 🧍 Classe base para o cliente
class Usuario:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def efetuar_operacao(self, conta, operacao):
        operacao.executar(conta)

    def vincular_conta(self, conta):
        self.contas.append(conta)

# 👤 Subclasse para pessoa física
class PessoaFisica(Usuario):
    def __init__(self, nome, nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf

# 🏦 Classe base para contas bancárias
class ContaBancaria:
    def __init__(self, numero, usuario):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._usuario = usuario
        self._extrato = Extrato()

    @classmethod
    def criar_conta(cls, usuario, numero):
        return cls(numero, usuario)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def usuario(self):
        return self._usuario

    @property
    def extrato(self):
        return self._extrato

    def sacar(self, valor):
        if valor <= 0:
            print("\n⚠️ Valor inválido para saque.")
            return False

        if valor > self._saldo:
            print("\n⚠️ Saldo insuficiente.")
            return False

        self._saldo -= valor
        print("\n✅ Saque realizado com sucesso.")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("\n⚠️ Valor inválido para depósito.")
            return False

        self._saldo += valor
        print("\n✅ Depósito realizado com sucesso.")
        return True

# 💳 Conta corrente com limites
class ContaCorrente(ContaBancaria):
    def __init__(self, numero, usuario, limite=500, max_saques=3):
        super().__init__(numero, usuario)
        self.limite = limite
        self.max_saques = max_saques

    def sacar(self, valor):
        saques_realizados = len([
            op for op in self.extrato.movimentos if op["tipo"] == Saque.__name__
        ])

        if valor > self.limite:
            print("\n⚠️ Valor excede o limite de saque.")
            return False

        if saques_realizados >= self.max_saques:
            print("\n⚠️ Número máximo de saques atingido.")
            return False

        return super().sacar(valor)

    def __str__(self):
        return f"""
Agência: {self.agencia}
Conta: {self.numero}
Titular: {self.usuario.nome}
"""

#  Registro de transações
class Extrato:
    def __init__(self):
        self._movimentos = []

    @property
    def movimentos(self):
        return self._movimentos

    def registrar_movimento(self, operacao):
        self._movimentos.append({
            "tipo": operacao.__class__.__name__,
            "valor": operacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })

#  Classe abstrata para operações
class Operacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def executar(self, conta):
        pass

#  Saque
class Saque(Operacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def executar(self, conta):
        if conta.sacar(self.valor):
            conta.extrato.registrar_movimento(self)

# Depósito
class Deposito(Operacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def executar(self, conta):
        if conta.depositar(self.valor):
            conta.extrato.registrar_movimento(self)