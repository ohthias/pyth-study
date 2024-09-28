import math

def calcular_area_circulo(raio):
    return math.pi * raio ** 2

def calcular_area_retangulo(largura, altura):
    return largura * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def main():
    print("Escolha o objeto para calcular a área:")
    print("1. Círculo")
    print("2. Retângulo")
    print("3. Triângulo")
    
    opcao = int(input("Digite o número da opção: "))
    
    if opcao == 1:
        raio = float(input("Digite o raio do círculo: "))
        area = calcular_area_circulo(raio)
        print(f"A área do círculo é: {area:.2f}")
        
    elif opcao == 2:
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = calcular_area_retangulo(largura, altura)
        print(f"A área do retângulo é: {area:.2f}")
        
    elif opcao == 3:
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"A área do triângulo é: {area:.2f}")
        
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
