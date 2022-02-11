import requests


def main():
    slip_id = input("Digite uma ID para receber uma frase motivacional aleatória (1-224): ")
    request = requests.get(f"https://api.adviceslip.com/advice/{slip_id}")

    slip = request.json()

    if "message" in slip:
        print("Número Inválido. Tente outro numero")
        main()
    else:
        print(f"Frase do ID [{slip['slip']['id']}]: {slip['slip']['advice']}\n")

    user_choose = input("Deseja sair do programa? 'SIM' ou 'NÃO': ")
    if user_choose.lower() == 'sim':
        print("Você escolheu sair")
        exit()

    main()


if __name__ == '__main__':
    main()
