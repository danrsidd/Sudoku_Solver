# Basic solver for 9x9 Sudoku with backtracking
puzzle = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

box1 = range(0,3) # Columns or Rows 0,1,2
box2 = range(3,6) # Columns or Rows 3,4,5
box3 = range(6,9) # Columns or Rows 6,7,8

def print_puzzle():
    for x in range(len(puzzle)):
        print(puzzle[x])

def boxChecker(pos):
    # Checks to see which of the 9 Sodoku boxes to loop through
    if pos in box1:
        p = box1
    elif pos in box2:
        p = box2
    else:
        p = box3
    return p

def puzzleFull():
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                return False
    return True

def emptyPos():
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return (i,j)
    return None

def possible(y,x,n):
    for i in range(len(puzzle)):
        # Check columns
        if puzzle[y][i] == n:
            return False
        # Check rows
        if puzzle[i][x] ==n:
            return False
        # Check 3x3 boxes 
        for j in boxChecker(y):
            for k in boxChecker(x):
                if puzzle[j][k] == n:
                    return False
    return True

def solve():
    if puzzleFull():
        print_puzzle()
    else:
        y,x = emptyPos()
        for i in range(1,10):
            if possible(y,x,i):
                puzzle[y][x] = i
                # Recursively call solve() with updated puzzle
                solve()
                # Backtrack any 'mistakes'
                puzzle[y][x] = 0

if __name__ == '__main__':
    solve()