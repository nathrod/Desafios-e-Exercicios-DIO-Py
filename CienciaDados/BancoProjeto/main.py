saldo = 1000.40
extrato = []
qnt_saque = 0

def Deposito():
    global saldo
    print("  \nDEPOSITO\n   ")
    valor_deposito = int(input("Valor R$ "))
    if valor_deposito<=0:
        print("Valor dever ser maior ou igual a zero!\n")
    else:
        saldo+=valor_deposito
        print("Deposito realizado com sucesso!\n Saldo atualizado R$ %.2f\n" %saldo)
        extrato.append("Valor Depositado R$ %.2f" %valor_deposito)
    op = None
    while op not in [0, 1]:
        op = int(input("\n0 - Voltar ao menu anterior\n1 - Realizar novo depósito\n"))
        if op == 0:
            Menu()
        elif op == 1:
            Deposito()
        else:
            print("Opção Inválida")

   
def Saque():
    global saldo
    global qnt_saque
    if qnt_saque>=3:
            print("Limite máximo diário atingindo\n")
            Menu()
    print("\nSAQUE")
    print("Limite Diário de 3 Saques. Valor da operação não deve ultrapassar R$ 500.00\n")
    valor_saque = int(input("Valor R$ "))
    if valor_saque>500 or valor_saque<=0:
        print("Por gentilza, insira um valor menor que R$ 500.00 e maior que R$ 0.00\n")
    elif valor_saque>saldo:
        print("Saldo Indisponivel, por gentileza, digite um valor menor ou igual a R$ %.2f" %saldo)
    else:
        saldo-=valor_saque
        print("Saque Realizado com sucesso!\n Saldo atualizado R$ %.2f\n" %saldo)
        qnt_saque+=1
        extrato.append("Saque Realizado R$ %.2f" %valor_saque)
    op = None
    while op not in [0, 1]:
        op = int(input("\n0 - Voltar ao menu anterior\n1 - Realizar novo saque\n"))
        if op == 0:
            Menu()
        elif op == 1:
            Saque()
        else:
            print("Opção Inválida")

def Extrato():
    global saldo
    global extrato
    print("\n     EXTRATO    ")
    print("\nSaldo Atual R$ %.2f" %saldo)
    for elemento in extrato:
        print(elemento)
    op = None
    while op not in [0, 1]:
        op = int(input("\n0 - Voltar ao menu anterior\n1 - Consultar Extrato Novamente\n"))
        if op == 0:
            Menu()
        elif op == 1:
            Extrato()
        else:
            print("Opção Inválida")
    
def Menu():
    print("      MENU      ")
    opcao = int(input("Selecione uma opção\n1-Realizar Deposito\n2-Realizar Saque\n3-Consultar Extrato\n"))

    if opcao==1:
        Deposito()
    elif opcao==2:
        Saque()
    elif opcao==3:
        Extrato()
    else:
        print("Opção Inválida\n")

Menu()