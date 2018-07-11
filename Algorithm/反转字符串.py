class Solution(object):
    def reverseString(self, s):
        s = list(s)
        longth = len(s) - 1
        for i in range(int(len(s)/2)):
            tmp = s[i]
            s[i] = s[longth-i]
            s[longth - i] = tmp
        str = ''.join(s)
        return str

s = Solution()
a = 'abc'
print(s.reverseString(a))
