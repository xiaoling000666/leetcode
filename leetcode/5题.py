class Solution(object):
    def longestPalindrome(self, s):
			new={}
			num=0
			jieguo=''
			for i,ch in enumerate(s):
				if ch in new and i-new[ch]>num:
					start=new[ch]
					end=i
					num=i-new[ch]
				new[ch]=i
			for i in range(start,end+1):
				jieguo=jieguo+s[i]
			print(jieguo)
a=Solution()
s='bababdfgavdfgdfgzfgfzfg'
a.longestPalindrome(s)
