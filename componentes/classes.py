from datetime import datetime as dt
class Usuario:
    def __init__(self, nome: str, cpf: str, data_nascimento: str, email: str, telefone: str, usuario: str, senha: str):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email = email
        self.telefone = telefone
        self.usuario = usuario
        self.senha = senha

    def __str__(self):
        return self.usuario
    
    def alterar_senha(self, nova_senha: str):
        self.senha = nova_senha

    def criar_conta(self):
        pass


class ContaBancaria:
    def __init__(self, conta: str):
        self.conta = conta
        self.saldo = 0
        self.extrato = {}

    def depositar(self, valor: float) -> bool:
        '''Deposita um valor na conta desde que seja positivo'''
        if valor < 0:
            self.saldo += valor
            self.extrato[dt.now()] = valor
            return True
        else:
            return False
    
    def sacar(self, valor: float) -> bool:
        '''Saca um valor da conta desde que seja menor que o saldo e maior que zero'''
        if self.saldo >= valor and valor > 0:
            self.saldo -= valor
            self.extrato[dt.now()] = -valor
            return True
        else:
            return False
        
    def mostrar_extrato(self):
        '''retorna uma lista de tuplas com o tipo de transação, a data e o valor, respectivamente'''
        return [("deposito", chave, valor) if valor > 0 else ("saque", chave, valor) for chave, valor in self.extrato.items()]
    

class ContaCorrente(ContaBancaria):
    def __init__(self, conta: str):
        super().__init__(conta)
        self.saques_diarios = 5
        self.limite_saque = 500

    def sacar(self, valor: float) -> bool:
        '''Saca um valor da conta desde que atenda aos requisitos de limite de saque'''
        if self.saques_diarios < sum(1 for chave, valor in self.extrato.items() if chave.date() == dt.now().date() and valor < 0):
            if valor <= self.limite_saque:
                super().sacar(valor)
                return True
            else:
                return False
        else:
            return False
    
    def alterar_limite_saque(self, novo_limite: float) -> bool:
        '''Altera o limite de saque da conta'''
        if self.saldo * 0.1 >= novo_limite:
            self.limite_saque = novo_limite
            self.saques_diarios = self.limite_saque // 100
            return True
        else:
            return False
