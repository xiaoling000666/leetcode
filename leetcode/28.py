class Solution(object):
    def strStr(self, haystack, needle):
        if needle == '':
            return 0
        if haystack==''or len(haystack)<len(needle):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1
s=Solution()
print s.strStr('hello','a')