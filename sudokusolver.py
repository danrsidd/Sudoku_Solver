'''Basic solver for 9x9 Sudoku with backtracking.'''

# Add 9x9 Sudoku puzzle here (can be edited to accomodate larger puzzles)
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

# Ranges representing the 9x9 puzzle grid (edit these to accomodate large puzzles)
box1 = range(0,3) # Columns or Rows 0,1,2
box2 = range(3,6) # Columns or Rows 3,4,5
box3 = range(6,9) # Columns or Rows 6,7,8

def print_puzzle():
    '''Uses global puzzle list and prints puzzle out, row by row.'''
    for x in range(len(puzzle)):
        print(puzzle[x])

def boxChecker(pos):
    '''Takes in y or x coordinate point and returns the 3x3 box the coordinate is located in.'''    
    if pos in box1:
        p = box1
    elif pos in box2:
        p = box2
    else:
        p = box3
    return p

def puzzleFull():
    '''
    Uses global puzzle list and returns whether the puzzle is full. 
    Returns True if there are no blanks (0's).
    '''
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                return False
    return True

def emptyPos():
    '''
    Uses global puzzle list and returns coordinate pair of next empty (0) space.
    Returns None if there are no empty spaces.
    '''
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return (i,j)
    return None

def possible(y,x,n):
    '''
    Takes in y (col) and x (row) coordinate of puzzle along with a number (n). 
    Returns whether it is possible to place n in given coordinate (True or False).
    '''
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
    '''
    Solves global puzzle list with a recursive backtracking approach. 
    Once the puzzle is full, the print_puzzle() function is called.
    '''
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