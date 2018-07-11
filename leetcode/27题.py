class Solution(object):
    def removeElement(self, nums, val):
        j=0
        h=0
        for i in range(len(nums)):
           if nums[i]!=val:
               nums[j]=nums[i]
               j=j+1
           else:
               h=h+1
        print len(nums)-h
s=Solution()
nums=[1]
val=1
s.removeElement(nums,val)