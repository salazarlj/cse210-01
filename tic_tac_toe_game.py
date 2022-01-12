
def main ():
    #This function will print title name.
    start_title()
    
    board = create_game_board()
    mark = change_player("")
   
    while not (win_a_game(board) or draw_game(board)):
        draw_interface(board)
        v_shift_player = mark_square(mark, board)
        if v_shift_player == 1:
            mark = change_player(mark)
        else:
            pass
    
    #Just I need to validate when a game is draw and Try error (if user type letter o type a wrong number -5 -6 10 11)
    
    draw_interface(board)
    if mark == "X":
        print("\n\t\tCONGRATULATION! --- PLAYER No2 WON")
    else:
        print("\n\t\tCONGRATULATION! --- PLAYER No1 WON")
    print("\t\tGREAT GAME. Thanks for playing!") 

def create_game_board():
    tic_tac_toe_board = []
    for square in range(9):
        tic_tac_toe_board.append(square + 1)
    return tic_tac_toe_board

def change_player(current_mark):
    if current_mark == "" or current_mark == "O":
        return "X"
    elif current_mark == "X":
        return "O"    

def start_title():
    print ("\n")
    print(" ┌████████████████████████████████████████████┐")
    print("██                                            ██")
    print("██            WELCOME GAME PLAYERS            ██")
    print("██              TIC-TAC-TOE GAME              ██")
    print("██════════════════════════════════════════════██")
    print("██ Tic-Tac-Toe is a game in which two players ██")
    print("██ seek in alternate turns to complete a row, ██")
    print("██ a column, or a diagonal with either three  ██")
    print("██ x's or three o's drawn in the spaces if a  ██")
    print("██ of a grid of nine squares.                 ██")
    print("██                                            ██")
    print(" └████████████████████████████████████████████┘")
    
def draw_interface(board):
     print ("\n")
     print("\t\t  ██  \t██\t\t")
     print(f"\t\t{board[0]} ██ {board[1]}\t██ {board[2]}\t\t")
     print("\t\t  ██  \t██\t\t")
     print("\t███████████████████████████")
     print("\t\t  ██  \t██\t\t")
     print(f"\t\t{board[3]} ██ {board[4]}\t██ {board[5]}\t\t")
     print("\t\t  ██  \t██\t\t")
     print("\t███████████████████████████")
     print("\t\t  ██  \t██\t\t")
     print(f"\t\t{board[6]} ██ {board[7]}\t██ {board[8]}\t\t")
     print("\t\t  ██  \t██\t\t")

def win_a_game(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def draw_game(board):
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
    return True 

def mark_square(v_mark, board):
    flag = 1
    if v_mark == "X":
        game_player = 1
    else:
        game_player = 2
      
    square = int(input(f"PLAYER #{game_player}: Choose a square (1-9) to mark '{v_mark}': "))
    v_validate = board [square-1]
    
    if (v_validate == "X" or v_validate == "O"):
        print ("SORRY, THIS SQUARE IS NOT AVIABLE. PLEASE, CHOOSE ANOTHER VALID POSITION")
        return 0
    else:
        #square - 1: Remember we are working with List, and Index starts in 0 position, so we need to subtrac
        board[square - 1] = v_mark
        return 1

if __name__ == "__main__":
    main()
