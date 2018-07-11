class Solution:
    def lengthOfLongestSubstring(self, s):
		new={}
		left=0
		num=0
		for i,ch in enumerate(s):
			if ch in new and new[ch]>=left:
				left=new[ch]+1
			new[ch]=i
			num=max(num,i-left+1)
		return(num)
a=Solution()
s='pwwkew'
a.lengthOfLongestSubstring(s)




