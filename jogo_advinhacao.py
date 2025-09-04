import random

def jogar():
    print("🎯 Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100")

    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            chute = int(input("Digite seu palpite: "))
        except ValueError:
            print("❌ Por favor, digite um número inteiro.")
            continue

        tentativas += 1

        if chute < numero_secreto:
            print("🔽 O número secreto é maior!")
        elif chute > numero_secreto:
            print("🔼 O número secreto é menor!")
        else:
            print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    jogar()

