def calculadora():
    print("=== Calculadora ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcao = input("\nEscolhe uma operação (1-4): ")
    
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    
    if opcao == "1":
        print(f"Resultado: {num1 + num2}")
    elif opcao == "2":
        print(f"Resultado: {num1 - num2}")
    elif opcao == "3":
        print(f"Resultado: {num1 * num2}")
    elif opcao == "4":
        if num2 == 0:
            print("Erro: não é possível dividir por zero!")
        else:
            print(f"Resultado: {num1 / num2}")
    else:
        print("Opção inválida!")

calculadora()
