class Solution(object):
    def isValid(self, s):
        dict = {')': '(', ']': '[', '}': '{'}
        pairs = []
        for c in s:
            if c in dict:
                if len(pairs)>=1 and dict[c]==pairs[-1]:
                    pairs.pop()
                else:
                    print 'false'
            else:
                pairs.append(c)
        if pairs==[]:
            print 'true'
        else:
            print 'false'
a=Solution()
s=']'
a.isValid(s)


