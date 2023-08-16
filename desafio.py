menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

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

    if opcao == "d":
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