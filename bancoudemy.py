from abc import ABC, abstractmethod

class Conta:
    
    def __init__ (self,agencia,nconta,saldo,senha):
        self.agencia = agencia
        self.nconta = nconta
        self.saldo = saldo
        self.senha = senha
        self.extrato = list()
        
    def depositar(self):
        global valor, senha 
        while True:
            valor = int(input('Quantos deseja depositar? >> \033[m R$ \033[m'))
            senha = int(input('Digite sua senha pra confirmar transação: '))
            if senha == self.senha:
                self.saldo += valor
                print('Transação conclúida.')
                self.extrato_(sinal='+',valor=valor)
                break
            else:
                print('Senha incorreta!')

    def get_saldo(self):
        print(f'Seu saldo atual é {self.saldo} ')
    
    @abstractmethod
    def sacar(self,valor):
        pass
  
    
    def extrato_(self,sinal:str,valor):
        self.extrato.extend([f'{sinal}{valor}'])
        
    def mostrar_extrato(self):
        print(f'EXTRATO:')
        for extrato in self.extrato:
            print(f'\t{extrato}')
            
class Conta_Corrente(Conta):
    def __init__(self,agencia,nconta,saldo,senha,limite):
        super().__init__(agencia,nconta,saldo,senha)
        self.limite = limite
    
    def sacar(self):
        valor = int(input('Quantos reais deseja sacar? '))
        if valor > self.saldo + self.limite:
            print(f'{valor} é um valor maior do que você pode sacar')
        elif self.saldo < valor < self.saldo + self.limite:
            self.saldo -= valor
            self.limite = (valor - self.saldo) - self.limite
            print('Transação conclúida')   
            self.extrato_(sinal='-',valor=valor)  
        elif valor < self.limite:
            self.saldo -= valor
            print('Transação concluída')
            self.extrato_(sinal='-',valor=valor)  

class Conta_Poupanca(Conta):
    def __init__(self,agencia,nconta,saldo,senha):
        super().__init__(agencia,nconta,saldo,senha)
        
    def sacar(self):
        valor = int(input('Quantos reais deseja sacar? '))
        if valor > self.saldo:
            print('Este valor é superior ao saldo da sua conta poupança.')
        else:
            self.saldo -= valor
            self.extrato_('-',valor)
    
class Pessoa(ABC):
    def __init__(self,idade,nome):
        self.idade = idade
        self.nome = nome
        
class Cliente(Pessoa):
    def __init__(self,idade,nome,conta):
        super().__init__(idade,nome)
        self.conta = conta #poupança ou corrente (agregação)
        

gabriel = Conta_Corrente(4342, '16452-90', 25000, 311006, 5000)
gabriel.sacar()
gabriel.depositar()
gabriel.sacar()
gabriel.mostrar_extrato()