class Solution():
    def main(self, s, target):
        s.sort()
        i = 0
        j = len(s)-1
        h = self.seek(s, target, i, j)
        return h

    def seek(self, s, target, i, j):
        m = i + (j - i)/2
        if i > j:
            return None
        else:
            if s[m] == target:
                return m
            elif s[m] > target:
                return self.seek(s, target, i, m-1)
            else:
                return self.seek(s, target, m+1, j)

a=Solution()
s = [1, 2, 3, 4 ,5]
target = 3
print(a.main(s, target))
