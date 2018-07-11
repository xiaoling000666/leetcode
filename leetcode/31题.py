# -*- coding: utf-8 -*
class Solution(object):
    def nextPermutation(self, nums):
        if len(nums)<=1:
            return
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                for j in range(len(nums)-1,i-1,-1):
                    if nums[j]>nums[i-1]:
                        a=nums[i-1]
                        nums[i-1]=nums[j]
                        nums[j]=a
                        nums[i:]=sorted(nums[i:])
                        break
                break
            if i==1:
                nums.sort()
        return nums

s=Solution()
nums=[4,6,5]
s.nextPermutation(nums)
