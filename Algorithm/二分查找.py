class Solution():
    def seek(self, s, target):
        i = 0
        j = len(s)-1
        while i < j:
            m = (i + j)//2
            if s[m] == target:
                return m
            elif s[m] > target:
                j = m-1
            else:
                i = m+1
        return None

a=Solution()
s = [1, 2, 3, 4, 5, 6]
target = 5
print(a.seek(s, target))
