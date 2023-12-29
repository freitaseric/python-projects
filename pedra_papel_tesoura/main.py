import random

user_choice = 0
bot_choice = 0

def startGame() -> None:
    print("Vamos começar!")
    print("A primeira jogada será sua, diga sua escolha!")
    
    user_choice = int(input("0 > Pedra\n1 > Papel\n2 > Tesoura\n"))
    bot_choice = random.randint(0, 2)

    choices = ['Pedra', 'Papel', 'Tesoura']
    user_choice_str = choices[user_choice]
    bot_choice_str = choices[bot_choice]

    if user_choice == bot_choice:
        print(f"Você escolheu {user_choice_str} e eu escolhi {bot_choice_str}, logo, empatamos!")
    elif (user_choice == 0 and bot_choice == 2) or (user_choice == 1 and bot_choice == 0) or (user_choice == 2 and bot_choice == 1):
        print(f"Você escolheu {user_choice_str} e eu escolhi {bot_choice_str}, logo, você ganhou!")
    else:
        print(f"Você escolheu {user_choice_str} e eu escolhi {bot_choice_str}, logo, você perdeu!")
        startGame()

startGame()