menu = """
[d] Depositar
[s] Sacar
[t] Transferir
[e] Extrato
[u] Histórico de Saques
[q] Sair

=> """

# Dados do usuário
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
historico_saques = []
saldo_outra_conta = 1000  # Saldo de uma conta para transferência

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

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
            historico_saques.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "t":
        valor = float(input("Informe o valor da transferência: "))

        if valor > 0 and valor <= saldo:
            saldo -= valor
            saldo_outra_conta += valor
            extrato += f"Transferência: R$ {valor:.2f}\n"
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso.")
        else:
            print("Operação falhou! Saldo insuficiente ou valor inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "u":
        print("\n===== Histórico de Saques =====")
        if historico_saques:
            for saque in historico_saques:
                print(saque)
        else:
            print("Nenhum saque realizado até agora.")
        print("===============================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
