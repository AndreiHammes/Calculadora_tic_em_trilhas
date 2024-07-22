def calculadora():
    while True:
        print("\nCalculadora simples\n")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("s. Sair")

        operacao = input("Selecione uma opçao ou 's' para sair: ")

        if operacao == 's' or operacao == 'S':
            print('Obrigado por utilizar a calculadora simpels')
            break
        
        if operacao not in ['1', '2', '3', '4']:
            print("Opção inválida, tente novamente!")
            continue    ## o conitnue reinicia o loop, diferente do break que sai do loop

        numero_1 = float(input("Primeiro número: "))
        numero_2 = float(input("Segundo número: "))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print(f"A soma de {numero_1} e {numero_2} é: {resultado}")
        elif operacao == '2':
            resultado = numero_1 - numero_2
            print(f"A subtração de {numero_1} e {numero_2} é : {resultado}")
        elif operacao == '3':
            resultado = numero_1 * numero_2
            print(f"A multiplicação de {numero_1} e {numero_2} é: {resultado}")
        else:
            if numero_2 == 0:
                print("Divisões por zero não são possíveis, tente novamente")
                continue
            else:
                resultado = numero_1 / numero_2
            print(f"A divisão de {numero_1} e {numero_2} é: {resultado}")

calculadora()