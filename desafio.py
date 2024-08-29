menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Valor que deseja depositar: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito +R${deposito:.2f} \n"
        else:
            print("Valor inválido, tente novamente.")
    
    elif opcao == "s":
        print("Saque")
        saque = float(input("Valor que deseja Sacar: "))
        if saque > saldo:
            print("Você não tem saldo suficiente.")

        elif saque > limite:
            print(f"Limite máximo por saque de R${limite:.2f}")

        elif numero_saques >= LIMITE_SAQUES:
            print("Número de saques excedido!")

        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque -R${saque:.2f} \n"
        
        else:
            print("Valor inválido, tente novamente.")
    
    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print(f"Saldo atual: R${saldo:.2f}")


    elif opcao == "q":
        break

    else:
        print("Opçãoo inválida, por favor selecione uma opção disponível.")
