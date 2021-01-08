def initial_state():
    arr=[]
    for i in range(3):
        col=[]
        for j in range(3):
            col.append(-1)
        arr.append(col)
    return arr

X=0
O=1

def player1(board):
    count=0
    for i in range(3):
        for j in range(3):
            if board[i][j] != -1:
                count=count+1
    if count%2 == 0:
        return 0
    else:
        return 1


EMPTY=-1

def terminal(board):
    if triplet_made(board):
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j]==-1:
                return False
    return True

def result(board,tup,player):
    if player:
        board[tup[0]][tup[1]]=1
    else:
        board[tup[0]][tup[1]]=0
    
    return board

def evaluate(my_board):

    for i in range(3):
        if my_board[i][0]==my_board[i][1] and my_board[i][1]==my_board[i][2]:
            if my_board[i][0] == 0:
                return -100
            elif my_board[i][0] == 1:
                return 100
    for j in range(3):
        if my_board[0][j] == my_board[1][j] and my_board[1][j] == my_board[2][j]:
            if my_board[0][j] == 0:
                return -100
            elif my_board[0][j] ==1:
                return 100
    if my_board[0][0] == my_board[1][1] and my_board[1][1] == my_board[2][2]:
        if my_board[0][0] == 0:
            return -100
        elif my_board[0][0] == 1:
            return 100
    if my_board[0][2] == my_board[1][1] and my_board[1][1] == my_board[2][0]:
        if my_board[0][2] == 0:
            return -100
        elif my_board[0][2] == 1:
            return 100
    return 0

def winner(board):
    score = evaluate(board)
    if score == 100:
        return "YOU"
    elif score == -100:
        return "Computer"
    else:
        return None


def triplet_made(my_board):
    for i in range(3):
        if my_board[i][0]==my_board[i][1] and my_board[i][1] == my_board[i][2]:
            if my_board[i][0] != -1:
                return True
    for j in range(3):
        if my_board[0][j]==my_board[1][j] and my_board[1][j] == my_board[2][j]:
            if my_board[0][j] != -1:
                return True
    if my_board[0][0]==my_board[1][1] and my_board[1][1] == my_board[2][2]:
        if my_board[0][0] != -1:
                return True
    if my_board[0][2]==my_board[1][1] and my_board[1][1] == my_board[2][0]:
        if my_board[0][2] != -1:
                return True
    
    return False

def func(my_board,depth,tup,maximize_bool,alpha,beta):# ai is 0-> minimizer => player is maximizer
   # print("func 1 is getting called with depth ",depth," ( ",tup[0]," , ",tup[1]," ) ",maximize_bool)
    if depth == 0 or triplet_made(my_board):                         
        return evaluate(my_board)+depth*10 ,tup
    x = -1
    y = -1
    answer = 0
    if maximize_bool:
        maxi = float('-inf')
        for i in range(3):
            for j in range(3):
                if my_board[i][j] == -1:
                    my_board[i][j] = 1
                    a,(m,n) = func(my_board,depth-1,(i,j),False,alpha,beta) 
                    if maxi < a:
                        maxi = a
                        answer=maxi
                        x = m 
                        y = n
                    my_board[i][j] = -1
                    alpha = max( alpha, maxi)
                    if beta <= alpha:
                        break
        

    else:
        mini = float('inf')
        for i in range(3):
            for j in range(3):
                if my_board[i][j] == -1:
                    my_board[i][j] = 0
                    a,(m,n)=func(my_board,depth-1,(i,j),True,alpha,beta)
                    if mini > a:
                        mini=a
                        answer=mini
                        x = m
                        y = n
                    my_board[i][j] = -1
                    beta = min( beta, mini)
                    if beta <= alpha:
                        break
    
    return answer,(x,y)

def minimax(board):
    depth=0#initialise
    my_board=[]
    for i in range(3):
        col = []
        for j in range(3):
            col.append(-1)
        my_board.append(col)
    for i in range(3):
        for j in range(3):
            if board[i][j]== 1:
                my_board[i][j]=1
            elif board[i][j] == 0:
                my_board[i][j]=0
            else:
                depth=depth+1
    mini=float("inf")
    x_final = -1# choosing random value just for scope of variable
    y_final = -1# choosing random value just for scope of variable
    for i in  range(3):
        for j in range(3):
            if my_board[i][j] == -1:
                my_board[i][j] = 0
                a , (x,y) = func(my_board,depth-1,(i,j),True,-float("inf"), float("inf"))
                if mini > a:
                    mini = a
                    x_final = i
                    y_final = j
                my_board[i][j] = -1      
    return (x_final,y_final)                                    