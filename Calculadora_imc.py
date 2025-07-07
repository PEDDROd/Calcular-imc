def calcular_imc():
    try:
        altura = float(input("digite a sua altura (ex: 1.75):"))
        peso = float(input("digite o seu peso (ex: 70.5):"))

        imc = peso / (altura** 2)
        imc = round(imc, 2)

        print(f"\nO IMC é: {imc}")

        if imc < 18.5:
            print("Classificação: Magreza")
        elif 18.5 <= imc <= 24.99:
            print("Classificação: Normal")
        elif 25 <= imc <=29.99:
            print("Classificação: Sobrepeso")
        elif 30 <= imc <= 34.99:
            print("Classificação: Obesidade Grau I")
        elif 35 <= imc <= 39.99:
            print("Classificação: Obesidade Grau II")
        else:
            print("Classificação: Obesidade Grau III")
    except ValueError:
        print("Por favor, digite valores válidos para altura e peso")
        
calcular_imc()
input('Pressione Enter para sair...')
