def initial_state():
    arr=[]
    for i in range(3):
        col=[]
        for j in range(3):
            col.append(-1)#change the elements at last to  'X' and 'O'
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
       # for i in range(3):
       #     for j in range(3):
       #         print(board[i][j],end=" ")
       #     print("")
       # print("triplet_made")
        return True
    # moves left

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

def evaluate(my_board):# optimise it later 
    # ai is 0
  #  for i in range(3):
  #      for j in range(3):
  #          print(my_board[i][j],end=" ")
  #      print("")
    for i in range(3):
        if my_board[i][0]==my_board[i][1] and my_board[i][1]==my_board[i][2]:
            if my_board[i][0] == 0:
                return -100
            elif my_board[i][0] == 1:
                return 100
    for j in range(3):
        if my_board[0][j] == my_board[1][j] and my_board[1][j] == my_board[2][j]:
            if my_board[0][i] == 0:
                return -100
            elif my_board[0][i] ==1:
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


"""
    count_0=0
    count_1=0
    for i in range(3):
        count_0=0
        count_1=0
        for j in range(3):
            if my_board[i][j] == 0:
                count_0 = count_0 + 1
            elif my_board[i][j] == 1:
                count_1 = count_1 + 1
        if count_0 == 3 and count_1 !=3 :
           # print("-100")
           # print("")
            return -100
        elif count_1 == 3 and count_0 !=3 :
           # print("100")
           # print("")
            return 100


    for j in range(3):
        count_0=0
        count_1=0
        for i in range(3):
            if my_board[i][j] == 0:
                count_0=count_0+1
            elif my_board[i][j] == 1:
                count_1 = count_1 +1
        if count_0 == 3 and count_1 !=3 :
          #  print("-100")
          #  print("")
            return -100
        elif count_1 == 3 and count_0 !=3 :
          #  print("100")
          #  print("")
            return 100


    count_0=0
    count_1=0
    for i in range(3):
        if my_board[i][i] == 0:
            count_0=count_0+1
        elif my_board[i][j] == 1:
            count_1 = count_1+1
    if count_0 == 3 and count_1 != 3:
      #  print("-100")
      #  print("")
        return -100
    elif count_1 == 3 and count_0 !=3:
      #  print("100")
      #  print("")
        return 100


    count_0=0
    count_1=0
    for i in range(3):
        if my_board[i][2-i]==0:
            count_0 = count_0+1
        elif my_board[i][2-i] == 1:
            count_1 = count_1+1
    if count_0 == 3:
      #  print("-100")
      #  print("")
        return -100
    elif count_1 == 3:
      #  print("100")
      #  print("")
        return 100
   # print("0")
   # print("")
    return 0
"""

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



def func(my_board,depth,tup,maximize_bool):# ai is 0-> minimizer => player is maximizer
   # print("func 1 is getting called with depth ",depth," ( ",tup[0]," , ",tup[1]," ) ",maximize_bool)
    if depth == 0 or triplet_made(my_board):                         
        return evaluate(my_board) ,tup
    x = -1
    y = -1
    answer = 0
    if maximize_bool:
        maxi = float('-inf')
        for i in range(3):
            for j in range(3):
                if my_board[i][j] == -1:
                    my_board[i][j] = 1
                    a,(m,n) = func(my_board,depth-1,(i,j),False) 
                    #print("a: ",a,"i: ",i,"j: ",j)
                    if maxi < a:
                        maxi = a
                        answer=maxi
                        x = m 
                        y = n
                    my_board[i][j] = -1
        

    else:
        mini = float('inf')
        for i in range(3):
            for j in range(3):
                if my_board[i][j] == -1:
                    my_board[i][j] = 0
                    a,(m,n)=func(my_board,depth-1,(i,j),True)
                    if mini > a:
                        mini=a
                        answer=mini
                        x = m
                        y = n
                    my_board[i][j] = -1
    return answer,(x,y)


def minimax(board):
   # print("minimax 1 is getting called")
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
 #   if my_board[1][1] ==- 1:
 #       return (1,1)
  #  print("minimax 2 is getting called")
    mini=float("inf")# lets build the part if ai is 'O'
    x_final = -1# choosing random value just for scope of variable
    y_final = -1# choosing random value just for scope of variable
   # print("For initial stage of my_board: ")
   # for i in range(3):
   #     for j in range(3):
   #         print(my_board[i][j],end=" ")
   #     print("")
    for i in  range(3):
        for j in range(3):
            if my_board[i][j] == -1:
               # print("minimax 3 inside loop is getting called")
                my_board[i][j] = 0
               # print("minimax 3 is getting called with depth ",depth," ( ",i," , ",j," ) ","True")
                a , (x,y) = func(my_board,depth-1,(i,j),True)
   #             print("a: ",a,"x; ",x,"y: ",y,"i: ",i,"j: ",j)
                if mini > a:
                    mini = a
                    x_final = i
                    y_final = j
                my_board[i][j] = -1                                 #this function will return score and position 
                                                                    # initially without aplha-beta puring 
                                                                    # making for ai = 0-> minimiser => real player is maximizer 
    #print("x_final",x_final,"y_final",y_final)
   # print(" ")
   # print("x_final",x_final,"y_final",y_final)
   # print(" mini",mini)
   # print(" ")
    return (x_final,y_final)                                    