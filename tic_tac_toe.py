def main():
    scoreboard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game_win = False
    player = "x"
    reset = False
    while game_win != True:
        showboard(scoreboard)
        print()
        action = int(input(f"{player}'s turn to choose a square (1-9): "))
        game_win, scoreboard, reset = update_board(scoreboard, player, action)
        if player == "x" and reset == False and game_win == False:
            player = "o"
        elif player == "o" and reset == False and game_win == False:
            player = "x"
    print(f"Player {player} wins!")

def showboard(scoreboard):
    print(f"{scoreboard[0]}|{scoreboard[1]}|{scoreboard[2]}")
    print(f"{scoreboard[3]}|{scoreboard[4]}|{scoreboard[5]}")
    print(f"{scoreboard[6]}|{scoreboard[7]}|{scoreboard[8]}")

def update_board(scoreboard, player, action):
    selected_move = action - 1
    if scoreboard[selected_move] == "x" or scoreboard[selected_move] == "o":
        print("That space is not available. Please choose another square.")
        return False, scoreboard, True
    else:
        scoreboard[selected_move] = player
        game_win, reset = win_check(scoreboard)
        return game_win, scoreboard, reset

def win_check(scoreboard):
    if scoreboard[0] == scoreboard[1] and scoreboard[1] == scoreboard[2]:
        return True, False
    elif scoreboard[3] == scoreboard[4] and scoreboard[4] == scoreboard[5]:
        return True, False
    elif scoreboard[6] == scoreboard[7] and scoreboard[7] == scoreboard[8]:
        return True, False
    elif scoreboard[0] == scoreboard[3] and scoreboard[3] == scoreboard[6]:
        return True, False
    elif scoreboard[1] == scoreboard[4] and scoreboard[4] == scoreboard[7]:
        return True, False
    elif scoreboard[2] == scoreboard[5] and scoreboard[5] == scoreboard[8]:
        return True, False
    elif scoreboard[0] == scoreboard[4] and scoreboard[4] == scoreboard[8]:
        return True, False
    elif scoreboard[2] == scoreboard[4] and scoreboard[4] == scoreboard[6]:
        return True, False
    else:
        return False, False



main()