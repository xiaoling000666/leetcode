class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        new_target=float('inf')
        for i in range(len(nums)-1):
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]<target and j<k:
                    if abs(nums[i]+nums[j]+nums[k]-target)<abs(new_target-target):
                        new_target = nums[i] + nums[j] + nums[k]
                    j += 1
                if nums[i]+nums[j]+nums[k]>target and j<k:
                    if abs(nums[i]+nums[j]+nums[k]-target)<abs(new_target-target):
                        new_target = nums[i] + nums[j] + nums[k]
                    k -= 1
                if nums[i]+nums[j]+nums[k]==target and j<k :
                    new_target=target
                    j+=1
                    k-=1
        return new_target
nums = [-1,2,1,-4]
target = 1
a=Solution()
a.threeSumClosest(nums,target)