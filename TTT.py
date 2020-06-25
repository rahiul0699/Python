# Tic Tac Toe Game
board = [" ",]*9
chance=1
p1='x'
p2='7'
mark=' '
won=1

def cont():
    global chance
    global board
    global won
    global board
    global value
    print("Do you want to continue Y or N")
    c=input()
    c=c.lower()
    if(c=='y'):
        board=[" ",]*9
        chance=1
        won=1
        choose()
def get():
    global chance
    global board
    
    if(chance % 2!=0):
        print("Chance for  "+p1)
        num=int(input())
        board[num-1]=p1
        mark=p1
        chance=chance+1
        decision(mark)
        

    else:
        print("Chance for "+p2)
        num=int(input())
        board[num-1]=p2 
        mark=p2
        chance=chance+1
        decision(mark)
    
    show() 
       

def show():
    global won
    global board
    
    print(board [0]+' | '+board [1]+' | '+board [2])
    print(board [3]+' | '+board [4]+' | '+board[5])
    print(board[6]+' | '+board[7]+' | '+board[8])
    if(won==1):
        get()
    

def decision(mark):
    global won
    global board
    
    if((board[0]==board[1]==board[2]==mark) or (board[3]==board[4]==board[5]==mark) or (board[6]==board[7]==board[8]==mark) or (board[0]==board[3]==board[6]==mark) or (board[1]==board[4]==board[7]==mark) or ( board[2]==board[5]==board[8]==mark) or (board[0]==board[4]==board[8]==mark) or (board[2]==board[4]==board[6]==mark)):
         print(mark +"has won the match")
         won=0
         show()
         cont()
    elif(" " not in board):
        print("The match is a draw")
        won=0
        show()
        cont()
    else:
        show()
        



def choose():
    global p1,p2
    print("Do you want X or O")
    p1= input()
    p1 = p1.lower()
    if(p1 == 'x'):
        p2 = 'o'
    else:
        p2 = 'x'
    print("Player 2 is "+p2)    
    show()


choose()
