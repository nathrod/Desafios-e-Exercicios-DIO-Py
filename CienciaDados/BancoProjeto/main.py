saldo = 1000.40
extrato = []
qnt_saque = 0

def Deposito():
    global saldo
    print("  \nDEPOSITO\n   ")
    
    valor_deposito = float(input("Valor R$ "))
    if valor_deposito<=0:
        print("Valor dever ser maior ou igual a zero!\n")
    else:
        saldo+=valor_deposito
        print("Deposito realizado com sucesso!\n Saldo atualizado R$ %.2f\n" %saldo)
        extrato.append("Valor Depositado R$ %.2f" %valor_deposito)
    
    voltar_menu = False
    while not voltar_menu:
        opcao = int(input("[0] Voltar ao menu principal\n[1] Realizar novo depósito\nSelecione uma opção: "))
        if opcao == 0:
            voltar_menu = True  # Sai do loop e volta ao menu principal
        elif opcao == 1:
            # Continua o loop e realiza um novo depósito
            valor_deposito = float(input("\nValor R$ "))
            if valor_deposito <= 0:
                print("Valor deve ser maior ou igual a zero!\n")
            else:
                saldo += valor_deposito
                print("Deposito realizado com sucesso!\nSaldo atualizado R$ %.2f\n" % saldo)
                extrato.append("Valor Depositado R$ %.2f" % valor_deposito)
        else:
            print("Opção inválida!")
   
def Saque():
    global saldo
    global qnt_saque
    if qnt_saque>=3:
            print("Limite máximo diário atingindo\n")
    print("\nSAQUE")
    print("Limite Diário de 3 Saques. Valor da operação não deve ultrapassar R$ 500.00\n")

    valor_saque = float(input("Valor R$ "))
    if valor_saque>500 or valor_saque<=0:
        print("Por gentileza, insira um valor menor que R$ 500.00 e maior que R$ 0.00\n")
    elif float(valor_saque)>float(saldo):
        print("Saldo Indisponivel, por gentileza, digite um valor menor ou igual a R$ %.2f" %saldo)
    else:
        saldo-=valor_saque
        print("Saque Realizado com sucesso!\n Saldo atualizado R$ %.2f\n" %saldo)
        qnt_saque+=1
        extrato.append("Saque Realizado R$ %.2f" %valor_saque)

    voltar_menu = False
    while not voltar_menu:
        opcao = int(input("[0] Voltar ao menu principal\n[1] Realizar novo saque\nSelecione uma opção: "))
        if opcao == 0:
            voltar_menu = True  # Sai do loop e volta ao menu principal
        elif opcao == 1:
            # Continua o loop e realiza um novo saque
            if qnt_saque>=3:
                print("Limite máximo diário atingindo\n")
            else: 
                valor_saque = float(input("\nValor R$ "))
                if valor_saque>500 or valor_saque<=0:
                    print("Por gentileza, insira um valor menor que R$ 500.00 e maior que R$ 0.00\n")
                elif float(valor_saque)>float(saldo):
                    print("Saldo Indisponivel, por gentileza, digite um valor menor ou igual a R$ %.2f" %saldo)
                else:
                    saldo-=valor_saque
                    print("Saque Realizado com sucesso!\n Saldo atualizado R$ %.2f\n" %saldo)
                    qnt_saque+=1
                    extrato.append("Saque Realizado R$ %.2f" %valor_saque)
        else:
            print("Opção inválida!")

def Extrato():
    global saldo
    global extrato
    print("\n     EXTRATO    ")
    print("\nSaldo Atual R$ %.2f" %saldo)
    for elemento in extrato:
        print(elemento)

def CadastrarUsuario():
    print("\n CADASTRO DE USUARIO \n")

def ContaBancaria():
    print("\n CADASTRAR CONTA BANCARIA \n")


def Menu():
    opcao = 0
    while opcao != 6:
        print("\n\nMENU")
        print("[1] Realizar Deposito\n[2] Realizar Saque\n[3] Consultar Extrato\n[4] Cadastrar Usuario\n[5] Cadastrar Conta Corrente\n[6] Sair\n")
        opcao = int(input("Selecione uma opção: "))

        if opcao==1:
            Deposito()
        elif opcao==2:
            Saque()
        elif opcao==3:
            Extrato()
        elif opcao==4:
            CadastrarUsuario()
        elif opcao==5:
            ContaBancaria()
        elif opcao==6:
            print("Saindo...")
        else:
            print("Opção Inválida\n")

Menu()
