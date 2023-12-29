from random import randint

choices = [1,2,3,4,5,6,7,8,9]
slots = ["", "", "", "", "", "", "", "", ""]
actual_player = "user"

def update_game_view(slots):
  if type(slots) != list:
    return
  
  print("Jogo da Velha")
  print("")
  print(f"     {slots[0]} | {slots[1]} | {slots[2]}     ")
  print("     ---------     ")
  print(f"     {slots[3]} | {slots[4]} | {slots[5]}     ")
  print("     ---------     ")
  print(f"     {slots[6]} | {slots[7]} | {slots[8]}     ")
  
  if actual_player == "user":
    send_choices(choices)

def make_play(player, position):
  global actual_player
  if player == "user":
    if len(slots[position-1]) == 0:
      slots[position-1] = "X"
      actual_player = "bot"
      update_game_view(slots)
      choiced = randint(0,8)
      make_play("bot", choiced)
    else:
      print("Você não pode jogar nessa posição!")
      update_game_view(slots)
  elif player == "bot":
    if len(slots[position-1]) == 0:
      slots[position - 1] = "O"
      actual_player = "user"
      update_game_view(slots)
    else:
      if "" in slots:
        choiced = randint(0,8)
        make_play("bot", choiced)
  else:
    return

def send_choices(choices):
  for i in range(5):
    print("")
  
  print("Faça sua escolha...")
  for c in choices:
    print(c)
  print("Digite 'sair' para sair do jogo!")
  print("Lembre-se que a contagem começa de cima para baixo e dá esquerda para a direita")
  choiced = input("Qual foi sua escolha? ")
  if choiced.lower() == "sair":
    print("Até mais!!")
    exit()
  make_play("user", int(choiced))

update_game_view(slots)
while True:  
  sequences = [[0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  
  if any(all(slots[i] == "X" for i in sequence) for sequence in sequences):
    print("Parabéns usuário, você venceu de mim!")
    break
  elif any(all(slots[i] == "O" for i in sequence) for sequence in sequences):
    print("Que pena usuário, você perdeu. Mas não fique triste, você foi um adversário formidável!")
    break
  elif all(len(slot) != 0 for slot in slots):
    print("O jogo acabou, o resultado final foi empate. Foi bom jogar com você!")
    break