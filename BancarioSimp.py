import datetime

class Usuario:
    usuarios = []
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        Usuario.usuarios.append(self)

class ContaCorrente:
    contas = []
    numero_conta_atual = 1
    def __init__(self, usuario):
        self.agencia = '008'
        self.numero_conta = ContaCorrente.numero_conta_atual
        ContaCorrente.numero_conta_atual += 1
        self.usuario = usuario
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.limite_diario_saque = 3000
        self.valor_sacado_hoje = 0
        self.data_ultimo_saque = None
        ContaCorrente.contas.append(self)
        print(f'Conta {self.numero_conta} criada para o usuário {self.usuario.nome} (CPF: {self.usuario.cpf}).')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append((valor, datetime.datetime.now()))
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso na conta {self.numero_conta}.')

    def sacar(self, valor):
        if self.data_ultimo_saque != datetime.date.today():
            self.valor_sacado_hoje = 0

        if valor > 0 and self.saldo >= valor and self.valor_sacado_hoje + valor <= self.limite_diario_saque:
            self.saldo -= valor
            self.saques.append((valor, datetime.datetime.now()))
            self.valor_sacado_hoje += valor
            self.data_ultimo_saque = datetime.date.today()
            print(f'Saque de R$ {valor:.2f} realizado com sucesso na conta {self.numero_conta}.')
        elif valor <= 0:
            print('O valor do saque deve ser positivo.')
        elif self.valor_sacado_hoje + valor > self.limite_diario_saque:
            print('Você atingiu o limite de saque diário de R$ 3.000,00.')
        else:
            print('Saldo insuficiente para realizar o saque.')

    def extrato(self):
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações.')
        else:
            print('Extrato:')
            print('| Tipo      | Valor     | Data e Hora         |')
            print('|-----------|-----------|---------------------|')
            movimentacoes = self.depositos + self.saques
            movimentacoes.sort(key=lambda x: x[1])
            for movimentacao in movimentacoes:
                data_hora = movimentacao[1].strftime("%d/%m/%Y %H:%M:%S")
                if movimentacao in self.depositos:
                    print(f'| Depósito  | R$ {movimentacao[0]:.2f} | {data_hora} |')
                else:
                    print(f'| Saque     | R$ {movimentacao[0]:.2f} | {data_hora} |')
            print(f'Saldo Atual: R$ {self.saldo:.2f}')

def criar_usuario(nome, data_nascimento, cpf, endereco):
    if cpf in [usuario.cpf for usuario in Usuario.usuarios]:
        print('CPF já cadastrado.')
    else:
        Usuario(nome, data_nascimento, cpf, endereco)

def criar_conta_corrente(cpf):
    usuario = next((usuario for usuario in Usuario.usuarios if usuario.cpf == cpf), None)
    if usuario is None:
        print('Usuário não encontrado.')
    else:
        ContaCorrente(usuario)
        print('Conta criada no banco 008 - O Banco de Futuro.')

# Uso do sistema
while True:
    print("\nEscolha uma operação:")
    print("1. Criar usuário")
    print("2. Criar conta corrente")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Visualizar Extrato")
    print("6. Sair")

    escolha = int(input("Digite o número da operação desejada: "))

    if escolha == 1:
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento do usuário (dd/mm/aaaa): ")
        cpf = input("Digite o CPF do usuário (somente números): ")
        endereco = input("Digite o endereço do usuário (Logradouro, Número - Bairro - Cidade - Estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)
    elif escolha == 2:
        cpf = input("Digite o CPF do usuário para criar a conta corrente (somente números): ")
        criar_conta_corrente(cpf)
    elif escolha == 3:
        cpf = input("Digite o CPF do usuário para depósito (somente números): ")
        numero_conta = int(input("Digite o número da conta para depósito: "))
        valor = float(input("Digite o valor para depósito: "))
        conta = next((conta for conta in ContaCorrente.contas if conta.usuario.cpf == cpf and conta.numero_conta == numero_conta), None)
        if conta is None:
            print('Esta conta não existe.')
        else:
            conta.depositar(valor)
    elif escolha == 4:
        cpf = input("Digite o CPF do usuário para saque (somente números): ")
        numero_conta = int(input("Digite o número da conta para saque: "))
        valor = float(input("Digite o valor para saque: "))
        conta = next((conta for conta in ContaCorrente.contas if conta.usuario.cpf == cpf and conta.numero_conta == numero_conta), None)
        if conta is None:
            print('Esta conta não existe.')
        else:
            conta.sacar(valor)
    elif escolha == 5:
        cpf = input("Digite o CPF do usuário para visualizar o extrato (somente números): ")
        numero_conta = int(input("Digite o número da conta para visualizar o extrato: "))
        conta = next((conta for conta in ContaCorrente.contas if conta.usuario.cpf == cpf and conta.numero_conta == numero_conta), None)
        if conta is None:
            print('Esta conta não existe.')
        else:
            conta.extrato()
    elif escolha == 6:
        print("Saindo do sistema.")
        break
    else:
        print("Operação inválida. Tente novamente.")
