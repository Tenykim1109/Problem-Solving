board = 0
res = 0
col = [0] * 12

def check(lv):
    global col
    
    for i in range(lv):
        if col[i] == col[lv] or abs(col[lv]-col[i]) == lv - i:
            return False
    
    return True

def nqueen(x):
    global board, res, col
    if x == board:
        res+=1
    else:
        for i in range(board):
            col[x] = i
            if check(x):
                nqueen(x+1)
        

def solution(n):
    global board, res
    board = n
    
    nqueen(0)
    
    return res