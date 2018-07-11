class Solution(object):
    def removeDuplicates(self, nums):
        j=0
        h=1
        if len(nums)==0:
            return []
        else:
            for i in range(1,len(nums)):
                if nums[i] != nums[j]:
                    nums[j+1]=nums[i]
                    j=j+1
                    h=h+1
        return h

s=Solution()
nums=[1,2,2,3,3,3,4,5,5,5,5,5,6]
s.removeDuplicates(nums)


