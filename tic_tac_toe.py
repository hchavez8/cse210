<<<<<<< HEAD
"""Author: Hayley Chavez
Tic-Tac-Toe is played according to the following rules.

The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a draw.

Requirements
Your program must also meet the following requirements.

The program must have a comment with assignment and author names.
The program must have at least one if/then block.
The program must have at least one while loop.
The program must have more than one function.
The program must have a function called main."""

grid_numbers = []
update = []

def main():
    print("Welcome to Tic Tac Toe! Player 1 is x's.")
    #grid_numbers = gameboard()
    #display_gameboard(gameboard())
    player = ""
    gameboard = create_gameboard()
    
    while not (winning_board(gameboard) or draw_board(gameboard)):
        player = player_marker(player)
        display_gameboard(gameboard)
        update_gameboard(gameboard, player)
        

    if winning_board:
        print(f"Congratulations, {player} wins!")
    elif draw_board:
        print(f"Nobody won. Try again.")

def create_gameboard():
    gameboard = [(i+1) for i in range(9)]
    return gameboard

def display_gameboard(gameboard):
    print(f"{gameboard[0]}|{gameboard[1]}|{gameboard[2]}")
    print("-+-+-")
    print(f"{gameboard[3]}|{gameboard[4]}|{gameboard[5]}")
    print("-+-+-")
    print(f"{gameboard[6]}|{gameboard[7]}|{gameboard[8]}")


def update_gameboard(gameboard, player_marker):
    
    player_action = int(input("Please choose a square 1-9: "))
    player_action = player_action - 1
    gameboard[player_action] = player_marker
    return gameboard

def winning_board(gameboard):
    return (gameboard[0] == gameboard[1] == gameboard[2] or
            gameboard[3] == gameboard[4] == gameboard[5] or
            gameboard[6] == gameboard[7] == gameboard[8] or
            gameboard[0] == gameboard[4] == gameboard[8] or
            gameboard[2] == gameboard[4] == gameboard[6] or
            gameboard[0] == gameboard[3] == gameboard[6] or
            gameboard[1] == gameboard[4] == gameboard[7] or
            gameboard[2] == gameboard[5] == gameboard[8])

def draw_board(gameboard):
    for i in range(9):
        if (gameboard[i] != "x" and gameboard[i] != "o"):
            return False
    return True

def player_marker(player):
    if player == "x":
        player = "y"
    elif player == "y" or player == "":
        player = "x"
    return player 

if __name__ == "__main__":
=======
"""Author: Hayley Chavez
Tic-Tac-Toe is played according to the following rules.

The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a draw.

Requirements
Your program must also meet the following requirements.

The program must have a comment with assignment and author names.
The program must have at least one if/then block.
The program must have at least one while loop.
The program must have more than one function.
The program must have a function called main."""
player_marker = ""
grid_numbers = []


def main():
    print("Welcome to Tic Tac Toe! Player 1 is x's.")
    grid_numbers = gameboard()
    display_gameboard(grid_numbers)

    while not winning_board or draw_board:
    #First turn
        update_gameboard(gameboard(), "x")
        display_gameboard(grid_numbers())
    
    #Second turn
        
        update_gameboard(gameboard(), "o")
        display_gameboard(gameboard)

    #Third turn
        player_action = int(input("Please choose a square 1-9: "))
        update_gameboard(player_action, gameboard(), "x")

    #Fourth turn

def gameboard():
    grid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return grid_numbers

def display_gameboard(gameboard):
    print(f"{grid_numbers[0]}|{grid_numbers[1]}|{grid_numbers[2]}")
    print("-+-+-")
    print(f"{grid_numbers[3]}|{grid_numbers[4]}|{grid_numbers[5]}")
    print("-+-+-")
    print(f"{grid_numbers[6]}|{grid_numbers[7]}|{grid_numbers[8]}")


def update_gameboard(gameboard, player_marker):
    player_action = int(input("Please choose a square 1-9: "))
    for i in gameboard:
        if player_action == i:
            i == player_marker

def winning_board(gameboard):
    return (gameboard[0] == gameboard[1] == gameboard[2] or
            gameboard[3] == gameboard[4] == gameboard[5] or
            gameboard[6] == gameboard[7] == gameboard[8] or
            gameboard[0] == gameboard[4] == gameboard[8] or
            gameboard[2] == gameboard[4] == gameboard[6] or
            gameboard[0] == gameboard[3] == gameboard[6] or
            gameboard[1] == gameboard[4] == gameboard[7] or
            gameboard[2] == gameboard[5] == gameboard[8])

def draw_board(gameboard):
    for i in gameboard:
        if gameboard[i] != "x" and gameboard[i] != "o":
            return False
        else:
            return True

if __name__ == "__main__":
>>>>>>> 4917460bc0188514463cc1584b49f98c866952a7
    main()