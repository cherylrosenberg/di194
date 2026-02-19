# Goal: Create a Tic Tac Toe game in Python where two players can play against each other.
# What you will create: A command-line Tic Tac Toe game that allows two players to take turns marking a 3x3 grid.

# Step 1: Representing the Game Board
# You’ll need a way to represent the 3x3 grid.
# A list of lists (a 2D list) is a good choice.
# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).

# game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Step 2: Displaying the Game Board
# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.
# Think about how to format the output to make it easy to read.

def display_board(board):
    # loop to iterate through each row
    print('*************')
    for i, row in enumerate(board):
        # Join elements of the row with a vertical bar
        print("* " + " | ".join(row) + " *")

        if i < 2:
            print("-------------")
    print('*************')

# Step 3: Getting Player Input
# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.

def player_input(player, board):
    while True: 
        try: 
            row_choice = int(input("What row would you like to play (1-3)? ")) - 1
            column_choice = int(input("What column would you like to play (1-3)? ")) - 1

            if row_choice not in [0,1,2] or column_choice not in [0,1,2]:
                print("Invalid input. Please choose numbers between 1 and 3")
                continue

            if board[row_choice][column_choice] != ' ':
                print("That spot is already taken! Try again.")
                continue
            
            board[row_choice][column_choice] = player
            break
        except ValueError:
            print("Please only enter valid numbers 1, 2, or 3")

# Step 4: Checking for a Winner
# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.

def check_win(board, player):
    #check rows
    for row in range(3): 
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True

    #check columns
    for column in range(3):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True

    #check diagonal 1
    if  board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True 

    #check diagonal 2
    if  board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True 

    return False

# Step 5: Checking for a Tie
# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.

def check_tie(board):
    for row in board: 
        if " " in row:
            return False
    return True

# Step 6: The Main Game Loop
# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).

def play():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = 'X'
    while True:
        display_board(board)
        player_input(player, board)

        if check_win(board,player):
            display_board(board)
            print(f"Player {player} wins!")
            break
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            break
        else: 
            if player == "X":
                player = "O"
            else:
                player = "X"

play()