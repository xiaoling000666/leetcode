class Solution:
    def permute(self, nums):
        l=[]
        self.res=[]
        self.DFS(nums, l)
        return self.res
    def DFS(self,nums,l):
        if nums==[]:
            self.res.append(l[:])
            #print self.res
        for i in range(len(nums)):
            l.append(nums[i])
            self.DFS(nums[:i]+nums[i+1:],l)
            l.pop()
nums=[1,1,2]
s=Solution()
print s.permute(nums)