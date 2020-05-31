from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_mark(mark):
   
    if mark == 'X':
        return ['X','O']
    else:
        return ['O','X']



def win(board, player):
    return (( board[7]==board[8]==board[9]==player) or
    ( board[4]==board[5]==board[6]==player) or 
    ( board[1]==board[2]==board[3]==player) or
    ( board[7]==board[4]==board[1]==player) or
    ( board[8]==board[5]==board[2]==player) or 
    ( board[9]==board[6]==board[3]==player) or
    ( board[1]==board[5]==board[9]==player) or
    ( board[3]==board[5]==board[7]==player))

def who_goes_first():
    if random.randint(0,1) == 0:
        return 'player_1'
    else:
        return 'player_2'

def move(board,letter,pos):
    board[pos] = letter

def space_free(board, pos):
    return board[pos] == ''

def get_move(board):
    pos=0 #instantiate it as an integer
    while pos not in range(1,10) or not space_free(board,pos):
 
        print('what is you next move '+turn+'?(1-9)')
 
        pos = int(input()) # if you don't transform it in an integer, it will never be able to compare it with range(1,10)
 
    return pos

def isboardfull(board):
    for i in range(1,10):
        if space_free(board,i):
            return False
    else:
        return True

print(" Welcome to TTT")

theboard = ['']*10
print("player1 choose your marker: X or O")
mark = input().upper()
    
player1,player2 = player_mark(mark) 
    
turn = who_goes_first()
print("the"+ turn+" will go first")
game_playing = True
while game_playing:
    if turn == 'player_1':
        display_board(theboard)
        pos = get_move(theboard)
        move(theboard, player1 , pos)
            
        if win(theboard, player1):
            display_board(theboard)
            print(" player1 wins")
            game_playing = False
        else:
            if isboardfull(theboard):
                print("its a tie")
                game_playing = False
                break;
            else:
                turn= 'player_2'
    else:
        display_board(theboard)
        pos = get_move(theboard)
        move(theboard, player2 , pos)
            
        if win(theboard, player2):
            display_board(theboard)
            print(" player2 wins")
            game_playing = False
        else:
            if isboardfull(theboard):
                print("its a tie")
                game_playing = False
                break
            else:
                turn = 'player_1'
            
                
        
               
            
            
        
        