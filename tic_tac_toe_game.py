
def main ():
    # Let us play a game called Tic-Tac-Toe. The game will change between one
    # player and the other. A bord is displayed where you choose a square with
    # a number.
    try:
        #This function will print a Title.
        start_title()
        
        #Let us to create a list of element to play our game.
        board = create_game_board()

        #Variable that helps us to change a mark (X or O) between players.
        mark = change_player("")
    
        #The main part of the program.
        while not (win_a_game(board) or draw_game(board)):
            draw_interface(board)
            v_shift_player = mark_square(mark, board)
            if v_shift_player == 1:
                mark = change_player(mark)
            else:
                pass
        
        draw_interface(board)
        if mark == "X":
            print("\n\t\tCONGRATULATION! --- PLAYER No2 WON")
        else:
            print("\n\t\tCONGRATULATION! --- PLAYER No1 WON")
        print("\t\tGREAT GAME. Thanks for playing!") 
    
    except IndexError as index_err:
        print("You has choosen an incorrect square(1-9).\n")
   
    except ValueError as v:
        print("Error - you entered a Character which is not a number.\n")
        
def create_game_board():
    """Create a list of elements to store numbers from 1 to 9.
    Paremeter: nothing.
    Return: List of elements to be used in the game board.
    """
    tic_tac_toe_board = []
    for square in range(9):
        tic_tac_toe_board.append(square + 1)
    return tic_tac_toe_board

def change_player(current_mark):
    """Let change the symnbol to be used in the game. When a player marks, the other player will need to use other mark.
    Paremeter: current_mark (the current mark did by a user)
    Return: A type of mark (X or O)
    """
    if current_mark == "" or current_mark == "O":
        return "X"
    elif current_mark == "X":
        return "O"    

def start_title():
    """Draw a special title for the program
    Paremeter: nothing.
    Return: nothing.
    """
    print ("\n")
    print("==============================================")
    print("|                                            |")
    print("|            WELCOME GAME PLAYERS            |")
    print("|              TIC-TAC-TOE GAME              |")
    print("|============================================|")
    print("| Tic-Tac-Toe is a game in which two players |")
    print("| seek in alternate turns to complete a row, |")
    print("| a column, or a diagonal with either three  |")
    print("| x's or three o's drawn in the spaces if a  |")
    print("| of a grid of nine squares.                 |")
    print("|                                            |")
    print("==============================================")
    
def draw_interface(board):
     """Draw a the interface for the game. In this case our board to mark.
    Paremeter: nothing.
    Return: nothing.
    """
     print ("\n")
     print("\t\t  |   \t| \t\t")
     print(f"\t\t{board[0]} |  {board[1]}\t|  {board[2]}\t\t")
     print("\t\t  |   \t| \t\t")
     print("\t===========================")
     print("\t\t  |   \t| \t\t")
     print(f"\t\t{board[3]} |  {board[4]}\t|  {board[5]}\t\t")
     print("\t\t  |   \t| \t\t")
     print("\t===========================")
     print("\t\t  |   \t| \t\t")
     print(f"\t\t{board[6]} |  {board[7]}\t|  {board[8]}\t\t")
     print("\t\t  |   \t| \t\t")

def win_a_game(board):
    """Verify if a diagonal row was filled. 
    Paremeter: board (list of elements marked with X's or O's)
    Return: true is some diagonal row was filled or false if not.
    """
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def draw_game(board):
    """Verify that an element from the list aren't market with Xs or Os
    Paremeter: board (list of elements marked with X's or O's)
    Return: true is all element aren't market or flase if not.
    """
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
    return True 

def mark_square(v_mark, board):
    """The main part of this program. Let us mark with X's or O's the element 
    of our List acording what player selected.
    Paremeter: 
    v_mark (it brings the type of mark to selec on the board)
    board  (board (list of elements marked with X's or O's)
    Return: a value to be used as a validation flag to continue in the same player.
    """
    flag = 1
    if v_mark == "X":
        game_player = 1
    else:
        game_player = 2
      
    square = int(input(f"PLAYER #{game_player}: Choose a square (1-9) to mark '{v_mark}': "))
    v_validate = board [square-1]
    
    if (v_validate == "X" or v_validate == "O"):
        print ("SORRY, THIS SQUARE IS NOT AVAILABLE. PLEASE, CHOOSE ANOTHER VALID POSITION")
        return 0
    else:
        # (square - 1): Remember we are working with List, and Index starts in 0 position, so we need to subtrac
        board[square - 1] = v_mark
        return 1

if __name__ == "__main__":
    main()