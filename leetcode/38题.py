class Solution(object):
    def countAndSay(self, n):
        string='1'
        while n>1:
            string=self.countStr(string)
            n=n-1
        return string
    def countStr(self,string):
        result=''
        count = 1
        for i in range(len(string)):
            if i<len(string)-1 and string[i]==string[i+1]:
                count=count+1
            else:
                result=result+str(count)+string[i]
                count = 1
        return result
s=Solution()
print s.countAndSay(6)