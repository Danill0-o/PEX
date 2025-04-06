import math

def calcular_placas_e_molduras():
    while True:
        print("Calculadora de Placas e Molduras de Gesso")
        print("-" * 40)

        # Entrada dos dados
        area_m2 = float(input("Informe a área total do forro (em m²): "))
        perimetro_m = float(input("Informe o perímetro total para molduras (em metros lineares): "))

        # Dimensões padrões
        area_placa = 0.6 * 0.6  # cada placa possui 0,36 m²
        comprimento_moldura = 1.2  # cada moldura possui 1,2 metros
        area_drywall = 1.2 * 1.8  # cada placa drywall possui 2,16 m²

        # Cálculo da quantidade necessária
        quantidade_placas = math.ceil(area_m2 / area_placa)
        quantidade_molduras = math.ceil(perimetro_m / comprimento_moldura)
        quantidade_drywall = math.ceil(area_m2 / area_drywall)

        # Exibição dos resultados
        print("\nResultados:")
        print(f"Quantidade de placas necessárias: {quantidade_placas} placas de 60cmx60cm")
        print(f"Quantidade de molduras necessárias: {quantidade_molduras} unidades de moldura")
        print(f"Quantidade de placas de drywall necessárias: {quantidade_drywall} placas de 120cmx180cm")

        # Opções para o usuário
        print("\nO que você deseja fazer agora?")
        print("1 - Realizar novo cálculo")
        print("2 - Sair")

        opcao = input("Digite sua opção (1 ou 2): ")

        if opcao == '2':
            print("Encerrando o programa...")
            break

if __name__ == "__main__":
    calcular_placas_e_molduras()

