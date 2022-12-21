"""
Tic Tac Toe
12/21/22
Daimler Garay
"""
import random as rd

gboard = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

current_player = "X"
winner = None
gameplay = True

# game board creation

def game_board(gboard):
    print(gboard[0] + " | " + gboard[1] + " | " + gboard[2])
    print("----------")
    print(gboard[3] + " | " + gboard[4] + " | " + gboard[5])
    print("----------")
    print(gboard[6] + " | " + gboard[7] + " | " + gboard[8])


# player move

def player_move(gboard):
    move = int(input("Enter a number between 1 - 9:\n"))
    if move >= 1 and move <= 9 and gboard[move-1] == "-":
        gboard[move-1] = current_player
    else:
        print("This spot is already occupied. Choose elsewhere.")

# checking for win

def horizontal_check(gboard):
    global winner
    if gboard[0] == gboard[1] == gboard[2] and gboard[0] != "-":
        winner = gboard[0]
        return True
    elif gboard[3] == gboard[4] == gboard[5] and gboard[3] != "-":
        winner = gboard[3]
        return True
    elif gboard[6] == gboard[7] == gboard[8] and gboard[6] != "-":
        winner = gboard[6]
        return True

def vertical_check(gboard):
    global winner
    if gboard[0] == gboard[3] == gboard[6] and gboard[0] != "-":
        winner = gboard[0]
        return True
    elif gboard[1] == gboard[4] == gboard[7] and gboard[1] != "-":
        winner = gboard[1]
        return True
    elif gboard[2] == gboard[5] == gboard[8] and gboard[2] != "-":
        winner = gboard[2]
        return True

def diagonal_check(gboard):
    global winner
    if gboard[0] == gboard[4] == gboard[8] and gboard[0] != "-":
        winner = gboard[0]
        return True
    elif gboard[2] == gboard[4] == gboard[6] and gboard[2] != "-":
        winner = gboard[2]
        return True

def tie_check(gboard):
    global gameplay
    if "-" not in gboard:
        game_board(gboard)
        print("It's a tie!")
        gameplay = False

def win_check():
    if diagonal_check(gboard) or horizontal_check(gboard) or vertical_check(gboard):
        print(f"The winner is {winner}")
        gameplay = False



# player switch

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# vs computer

def computer(gboard):
    while current_player == "O":
        pos = rd.randint(0, 8)
        if gboard[pos] == "-":
            gboard[pos] = "O"
            switch_player()
    

while gameplay:
    game_board(gboard)
    if winner != None:
        break
    player_move(gboard)
    win_check()
    tie_check(gboard)
    switch_player()
    computer(gboard)
    win_check()
    tie_check(gboard)