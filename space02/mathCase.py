def main():
    print("Escolha uma opção:")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Opção 3")
    
    opcao = input("Digite o número da opção: ")

    match opcao:
        case "1":
            print("Você escolheu a opção 1!")
        case "2":
            print("Você escolheu a opção 2!")
        case "3":
            print("Você escolheu a opção 3!")
        case _:
            print("Opção inválida!")

if __name__ == "__main__":
    main()