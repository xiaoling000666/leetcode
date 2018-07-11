class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix_new = []
        list = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                list.append(0)
            matrix_new.append([list])
        return matrix_new

matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
s=Solution()
print(s.rotate(matrix))