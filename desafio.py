menu = """
[u] Criar usuário
[a] Criar conta corrente

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

usuarios = []
numero_conta = 0
contas = []

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def criar_usuario(*, valor, usuarios):
    nome = input("Digite o seu nome: ")
    data_de_nascimento = input("Digite a sua data de nascimento (formato: dd/mm/yyyy): ")
    endereco = input("Digite o seu endereço (logradouro, nº - bairro - cidade/sigla estado): ")
    usuarios.append({
        "Nome": nome,
        "Data de nascimento": data_de_nascimento,
        "CPF": valor,
        "Endereço": endereco
    })
    print(f"Usuário {valor} cadastrado com sucesso!")
    return usuarios

def criar_conta(*, usuario, numero_conta, contas):
    contas.append({
        "Agência": "0001",
        "Número da conta": numero_conta,
        "Usuário": usuario
    })
    return contas

def depositar(*, valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")
        return False

def sacar(valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato, /):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return False

def tirar_extrato(*, extrato, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:

    opcao = input(menu)

    if opcao == "u":
        valor = input("Digite seu CPF (apenas números): ")
        for usuario in usuarios:
            if usuario.get("CPF") == valor:
                print("Operação falhou! CPF já está cadastrado no sistema!")
                break
        else:
            usuarios = criar_usuario(valor=valor, usuarios=usuarios)

    elif opcao == "a":
        valor = input("Digite seu CPF (apenas números): ")
        for usuario in usuarios:
            if usuario.get("CPF") == valor:
                numero_conta += 1;
                contas = criar_conta(usuario=usuario, numero_conta=numero_conta, contas=contas)
                print(f"Conta criada com sucesso!")
                break
        else:
            print("Operação falhou! CPF não existe!")

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        resultado = depositar(valor=valor, saldo=saldo, extrato=extrato)
        if resultado:
            saldo = resultado[0]
            extrato = resultado[1]

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        resultado = sacar(valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato)
        if resultado:
            saldo = resultado[0]
            extrato = resultado[1]
            numero_saques = resultado[2]

    elif opcao == "e":
        tirar_extrato(extrato=extrato, saldo=saldo)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")