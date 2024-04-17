from collections import defaultdict


def isValidSudoku(board):
    # create 3 hash-sets as follows for storing the values corresponding to each row, column and 3X3 sub board -->
    
    row_dict = defaultdict(set)  # key = row number , value = set which will contain the values in that particular row
    
    col_dict = defaultdict(set)  # key = column number , value = set which will contain the values in that particular column
    
    sub_board_dict = defaultdict(set)  # key = tuple (row // 3, col // 3 ) ,  value = set which will contain the values in that particular 3 X 3 board 
    
    # * We can name each sub box by (0,0) , (0,1) , (0,2) ..... (2,2) -> By taking integer division by 3
    
    for i in range(9):
        for j in range(9):
            
            # neglect empty values
            if board[i][j] == ".":
                continue
            
            # simply return if there exists duplicate values 
            if  (
                board[i][j] in row_dict[i] or 
                board[i][j] in  col_dict[j] or 
                board[i][j] in sub_board_dict[(i//3, j//3)]
            ):
                return False
            
            else:
                row_dict[i].add(board[i][j])
                col_dict[j].add(board[i][j])
                sub_board_dict[(i//3, j//3)].add(board[i][j])
                
    return True



print(isValidSudoku([
    ["5","3",".",".","7",".",".",".","."]
,   ["6",".",".","1","9","5",".",".","."]
,   [".","9","8",".",".",".",".","6","."]
,   ["8",".",".",".","6",".",".",".","3"]
,   ["4",".",".","8",".","3",".",".","1"]
,   ["7",".",".",".","2",".",".",".","6"]
,   [".","6",".",".",".",".","2","8","."]
,   [".",".",".","4","1","9",".",".","5"]
,   [".",".",".",".","8",".",".","7","9"]]))