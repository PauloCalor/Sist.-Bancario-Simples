# Sist.-Bancario-Simples
Sistema Bancario simples em Python

O principal objetivo deste código é simular um sistema bancário básico. Ele permite a criação de usuários e contas correntes, além de realizar operações bancárias como depósitos, saques e visualização de extratos. Aqui estão as principais funcionalidades:

Criação de usuários: Cada usuário tem um nome, data de nascimento, CPF e endereço. A função criar_usuario permite adicionar novos usuários ao sistema.
Criação de contas correntes: Cada conta corrente está associada a um usuário e tem um número de conta, saldo e histórico de transações (depósitos e saques). A função criar_conta_corrente permite criar novas contas para os usuários.
Depósitos: Os usuários podem depositar dinheiro em suas contas. O valor do depósito é adicionado ao saldo da conta e a transação é registrada.
Saques: Os usuários podem sacar dinheiro de suas contas, desde que o valor do saque não exceda o saldo da conta nem o limite diário de saque.
Extrato: Os usuários podem visualizar um extrato de suas contas, que lista todas as transações de depósito e saque realizadas, bem como o saldo atual.
Interface de usuário: O código inclui um loop principal que apresenta ao usuário uma lista de operações que ele pode realizar (criar usuário, criar conta corrente, depositar, sacar, visualizar extrato, sair) e solicita que ele escolha uma. Dependendo da escolha do usuário, a operação correspondente é realizada.
