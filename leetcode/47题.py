class Solution:
    def permute(self, nums):
        l=[]
        nums.sort()
        self.res=[]
        self.DFS(nums, l)
        return self.res
    def DFS(self,nums,l):
        if nums==[]:
            self.res.append(l[:])
            print(self.res)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                print(nums,nums[i])
                continue
            l.append(nums[i])
            print(l,i)
            self.DFS(nums[:i]+nums[i+1:],l)
            l.pop()
nums=[3,3,0,3]
s=Solution()
print(s.permute(nums))