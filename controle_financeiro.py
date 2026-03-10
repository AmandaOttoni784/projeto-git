print(" CONTROLE FINANCEIRO ")

salario = float(input("Digite seu salário mensal: "))

gastos = []

while True:

    print("\nMENU")
    print("1 - Adicionar gasto")
    print("2 - Ver gastos")
    print("3 - Ver resumo do mês")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do gasto : ")
        valor = float(input("Digite o valor do gasto: "))

        gastos.append((nome, valor))

        print("Gasto adicionado com sucesso!")

    elif opcao == "2":
        print("\nLista de gastos:")

        if len(gastos) == 0:
            print("Nenhum gasto registrado.")
        else:
            for i, gasto in enumerate(gastos, start=1):
                nome, valor = gasto
                print(f"{i} - {nome}: R$ {valor:.2f}")

            print(f"\nTotal de gastos registrados: {len(gastos)}")

    elif opcao == "3":
        if len(gastos) == 0:
            print("Nenhum gasto registrado.")
        else:
            valores = [valor for nome, valor in gastos]

            total = sum(valores)
            maior = max(valores)
            menor = min(valores)
            media = total / len(valores)
            restante = salario - total

            print("\n===== RESUMO =====")
            print(f"Total gasto: R$ {total:.2f}")
            print(f"Quantidade de gastos: {len(gastos)}")
            print(f"Maior gasto: R$ {maior:.2f}")
            print(f"Menor gasto: R$ {menor:.2f}")
            print(f"Média de gastos: R$ {media:.2f}")
            print(f"Dinheiro restante: R$ {restante:.2f}")

            if total > salario:
                print("⚠ Atenção! Você gastou mais que seu salário!")
            elif restante < salario * 0.2:
                print("⚠ Cuidado! Você está perto de gastar todo o salário.")
            else:
                print("✅ Suas finanças estão sob controle!")

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")