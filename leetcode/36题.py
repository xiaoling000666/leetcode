class Solution(object):
    def isValidSudoku(self,list):
        s=set()
        for i in range(9):
            for j in range(9):
                if list[i][j] in s:
                    return False
                if list[i][j]!='.':
                    s.add(list[i][j])
            s = set()
        for i in range(9):
            for j in range(9):
                if list[j][i] in s:
                    return False
                if list[j][i]!='.':
                    s.add(list[j][i])
            s = set()
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        if list[m][n] in s:
                            return False
                        if list[m][n] != '.':
                            s.add(list[m][n])
                s = set()
        return True
s=Solution()
board=[[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
print s.isValidSudoku(board)

