print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {"rock": 1, "scissors": 2, "paper": 3}
    player_one = str(input("Player 1: "))
    player_two = str(input("Player 2: "))
    a = game_dict.get(player_one)
    b = game_dict.get(player_two)
    dif = a - b

    if dif in [-1, 2]:
        print("Player One Wins.")
        if str(input("Do you want to play another game, Y or N?\n")) == "Y" or "yes":
            continue
        else:
            print("Game Over.")
            break
    elif dif in [-2, 1]:
        print("Player Two Wins.")
        if str(input("Do you want to play another game, Y or N?\n")) == "Y" or "yes":
            continue
        else:
            print("Game Over.")
            break
    else:
        print("Draw. Please try again.")
        print("")
