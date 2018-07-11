class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ''
        if strs == []:
            return result
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
            count = 0
            for j in range(len(strs)-1):
                if i == len(strs[j]) or i == len(strs[j+1]):
                    return result
                if strs[j][i] != strs[j+1][i]:
                    return result
            result = result + strs[j][i]
        return result
strs = ['a']
s = Solution()
print(s.longestCommonPrefix(strs))