class Solution(object):
    def solveSudoku(self, board):
        def isvaild(i,j):
            for m in range(9):
                if m!=i and board[m][j]==board[i][j]:
                    return False
            for n in range(9):
                if n!=j and board[i][n]==board[i][j]:
                    return False
            for m in range(i/3*3,i/3*3+3):
                for n in range(j/3*3,j/3*3+3):
                    if m!=i and n!=j and board[m][n]==board[i][j]:
                        return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    for c in '123456789':
                        board[i][j]=c
                        if isvaild(i,j):
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = '.'
                        else:
                            board[i][j] = '.'
                    return False
        return True
s=Solution()
board=[[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
print s.solveSudoku(board)
