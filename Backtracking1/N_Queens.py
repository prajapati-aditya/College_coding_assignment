n = 4
board = [["."] * n for _ in range(n)]
#print(board)


sol = []

col = set()
diag1 = set()
diag2 = set()

def dfs (r) :
    # base case
    if r == n :
        temp = ["".join (row) for row in board]
        sol.append(temp)
        return

    for c in range (n) :
        if c in col or (r-c) in diag1 or (r+c) in diag2 :
            continue
        # place the queen here
        board[r][c] = 'Q'
        col.add(c)
        diag1.add(r-c)
        diag2.add(r+c)
        print(diag1)
        # check for other
        dfs(r+1)
        # remove the queen
        board[r][c] = '.'
        col.remove(c)
        diag1.remove(r-c)
        diag2.remove(r+c)
dfs(0)
print(sol)