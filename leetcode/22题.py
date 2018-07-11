class Solution(object):
    def generateParenthesis(self,n):
        self.res = []
        self.dfs("",n,n)
        print self.res
    def dfs(self,mmmm,l,r):
        if r==0 and l==0:
            self.res.append(mmmm)
        if l>0:
            self.dfs(mmmm+'(',l-1,r)
        if r>0 and r>l:
            self.dfs(mmmm+')',l,r-1)
s=Solution()
a=2
s.generateParenthesis(a)

