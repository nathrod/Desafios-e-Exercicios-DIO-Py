import sys

usuarios = [46030810812]
cadastro = {46030810812: [['Nathalia Rodrigues', '18/10/1999', 'Rua José do Nascimento, 309 - Jardim São Paulo- Itapiri/SP']]}
contas = [[46030810812,1,"0001",0,0,[]],[30820840898,2,"0001",200,0,[]],[46030810812,3,"0001",650,0,[]]] 
#         [cpf, número da conta, agência, saldo,saques_realizados,extrato=[]]

def Deposito(saldo, valor_deposito,extrato):
    
    if valor_deposito<=0:
        print("Valor dever ser maior ou igual a zero!\n")
    else:
        saldo+=valor_deposito
        print("Deposito realizado com sucesso!\n Saldo atualizado R$ %.2f\n" %saldo)
        extrato.append("Valor Depositado R$ %.2f" %valor_deposito)

    return saldo,extrato
   
def Saque(*,saldo, valor, limite, saques_realizados,extrato):

    if saques_realizados==3:
            print("Limite máximo diário atingindo\n")
    else:
        if float(valor)>float(saldo):
            print("Saldo Insuficiente!\n") 
        elif valor>limite or valor<=0:
            print("Por gentileza, insira um valor menor que R$ 500.00 e maior que R$ 0.00\n")
        else:
            saldo-=valor
            saques_realizados+=1
            print("Saque Realizado com sucesso!\n Saldo atualizado R$ %.2f\n" %saldo)
            extrato.append("Saque Realizado R$ %.2f" %valor)

    return saldo,saques_realizados,extrato

def Extrato(saldo,/,*,extrato): 

    print("\n     EXTRATO    ")
    print("\nSaldo Atual R$ %.2f" %saldo)
    for elemento in extrato:
        print(elemento)

def CadastrarUsuario():
    print("\n CADASTRO DE USUARIO \n")
    global usuarios
    global cadastro
    
    cpf = int(input("\nCPF (11 digitos): "))
    verificarCPF(cpf)

    if cpf in usuarios:
        print("\nCPF já cadastrado!\n")
    else:
        usuarios.append(cpf)
        info = []
        nome = input("Nome: ")
        info.append(nome)
        data_nascimento = input("Data de Nascimento: ")
        info.append(data_nascimento)
        endereco = input("Endereço (logradouro,nro - bairro - cidade/SP): ")
        info.append(endereco)
            
        cadastro[cpf] = [info]
        print("Cadastro realizado com sucesso!\n")
    
    for chave in cadastro:
        print(chave,cadastro[chave])

def ContaBancaria():
    print("\n CADASTRAR CONTA BANCARIA \n")
    #CPF estão na lista usuários
    global contas
    global usuarios

    cpf = int(input("CPF (11 digitos): "))
    verificarCPF(cpf)

    if cpf not in usuarios:
        print("Usuario não cadastrado!\n")
        sys.exit()
    else:
        user = []
        user.append(cpf)
        user.append(len(contas)+1) # Conta 1,2,3. Indice mais 1
        user.append("0001") # Agencia
        user.append(float(0)) # Saldo conta[user-1][3]
        user.append(0) # quantidade de saques, começa com 0
        user.append([]) # extrato que é uma lista vazia
        contas.append(user)

    print("\nContas cadastradas: \n")
    print(contas)

def ConsultarUsuarios():
    global cadastro
    print("\n CONSULTAR USUÁRIOS \n")
    cpf = int(input("CPF (11 digitos): "))
    verificarCPF(cpf)

    if cpf not in cadastro:
        print("Usuario não cadastrado!\n")
        sys.exit()
    else:
        print(cpf,cadastro[cpf])

def verificarCPF(cpf):
    cpf_str = str(cpf)
    tamanho = list(cpf_str)
    if (len(tamanho)<11) or (len(tamanho)>11):
        print("CPF Inválido!\n")
        sys.exit()

def SelecionarConta(cpf):

    #Mostrar as contas relacionadas aquele CPF
    #Listar todas as listas dentro da lista conta que possui o CPF que o usuário digitar
    lista_cpf_escolhido = []

    for lista in contas:
        if lista[0] == cpf:
            lista_cpf_escolhido.append(lista)

    if len(lista_cpf_escolhido)==0:
        print(f"Nenhuma conta encontrada para o CPF {cpf}\n")
        sys.exit()
    else:
        print(f"\nContas Pertencentes ao CPF {cpf}")
        for indice, lista in enumerate(lista_cpf_escolhido):
            print(f"{indice}: {lista}")
            
        #Selecionar a conta desejada
        op = int(input("\nSelecione a conta desejada: "))
        saldo = lista_cpf_escolhido[op][3]
        saques_realizados = lista_cpf_escolhido[op][4]
        extrato = lista_cpf_escolhido[op][5]
    return saldo,saques_realizados,extrato

def Menu():
    opcao = 0
    while opcao != 7:
        print("\n\nMENU")
        print("[1] Realizar Deposito\n[2] Realizar Saque\n[3] Consultar Extrato\n[4] Cadastrar Usuario\n[5] Cadastrar Conta Corrente\n[6] Consultar Usuário\n[7] Sair\n")
        opcao = float(input("Selecione uma opção: "))

        if opcao==1:
            print("REALIZAR DEPOSITO")
            cpf = int(input("CPF (11 digitos): "))
            verificarCPF(cpf)

            saldo,saques_realizados,extrato = SelecionarConta(cpf)
            valor_deposito = float(input("Valor R$ "))
            for lista in contas:
                if lista[0]==cpf and lista[3]==saldo:
                    saldo_atualizado,extrato_atualizado = Deposito(saldo, valor_deposito,extrato)
                    lista[3] = saldo_atualizado
                    lista[5] = extrato_atualizado
            print(contas)
        elif opcao==2:
            print("\nSAQUE")
            print("Limite Diário de 3 Saques. Valor da operação não deve ultrapassar R$ 500.00\n")
            cpf = int(input("CPF (11 digitos): "))
            verificarCPF(cpf)

            saldo,qntd,extrato = SelecionarConta(cpf)
            valor_saque = float(input("Valor R$ "))
            for lista in contas:
                if lista[0]==cpf and lista[3]==saldo and lista[4]==qntd:
                    saldo_atualizado,qntd_atualizada,extrato_atualizado = Saque(saldo=saldo,valor=valor_saque,limite=500,saques_realizados=qntd,extrato=extrato)
                    lista[3] = saldo_atualizado
                    lista[4] = qntd_atualizada
                    lista[5] = extrato_atualizado
            print(contas)
        elif opcao==3:
            cpf = int(input("CPF (11 digitos): "))
            saldo,qntd,extrato = SelecionarConta(cpf)
            Extrato(saldo,extrato=extrato)
        elif opcao==4:
            CadastrarUsuario()
        elif opcao==5:
            ContaBancaria()
        elif opcao==6:
            ConsultarUsuarios()
        elif opcao==7:
            print("Saindo...")
        else:
            print("Opção Inválida\n")

Menu()