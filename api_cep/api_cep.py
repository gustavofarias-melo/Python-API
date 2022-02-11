import requests


def main():
    print("=======================")
    print("|||  BUSCA POR CEP  |||")
    print("=======================")

    print("Coloque o CEP abaixo, exemplo: 55790000)")
    cep_user = input("Digite o cep: ")

    if len(cep_user) != 8:
        print("Por favor, digite os 8 dígitos do CEP")
        main()

    request = requests.get(f"https://viacep.com.br/ws/{cep_user}/json/")

    address = request.json()

    if 'erro' in address:
        print("CEP Inválido")
    else:
        print(f"CEP: {address['cep']}")
        print(f"Logradouro: {address['logradouro']}")
        print(f"Bairro: {address['bairro']}")
        print(f"Estado: {address['uf']}")
        print(f"Localidade: {address['localidade']}")
        print(f"DDD: {address['ddd']}")

    user_choose = int(input("Deseja inserir outro CEP?\n 1.SIM \n 2.NÂO\n"))
    if user_choose == 1:
        main()
    else:
        print("Você decidiu sair.")
        exit()


if __name__ == '__main__':
    main()
