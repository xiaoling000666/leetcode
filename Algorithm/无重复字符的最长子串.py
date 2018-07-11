class Solution():
    def lengthOfLongestSubstring(self, s):
        list_num=[]
        list_char=[]
        sum = 1
        a = s[0]
        for i in range(1,len(s)):
            if s[i]!=s[i-1] and s[i] not in a:
                sum = sum+1
                a = a + s[i]
            else:
                list_num.append(sum)
                list_char.append(a)
                sum = 1
                a = s[i]
        j = max(list_num, list_char)
        return list_num, list_char
a = Solution()
s='abcabcbb'
print(a.lengthOfLongestSubstring(s))



