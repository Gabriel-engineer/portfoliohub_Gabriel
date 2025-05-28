#CALCULADORA SIMPLES

def adicionar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        return "Erro! Divisão por zero não é permitida."
    return n1 / n2

def exibir_menu():
    print("\nSelecione a operação desejada:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

def main():
    print("Bem-vindo à Calculadora Dinâmica!")

    while True:
        exibir_menu()
        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            print("Obrigado por usar a calculadora. Até logo!")
            break

        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, insira números.")
                continue

            if escolha == '1':
                print(f"\nResultado: {num1} + {num2} = {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"\nResultado: {num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"\nResultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                resultado_divisao = dividir(num1, num2)
                print(f"\nResultado: {num1} / {num2} = {resultado_divisao}")
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":

    main()

