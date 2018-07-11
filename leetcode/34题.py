class Solution(object):
    def searchRange(self, nums, target):
        start=0
        end=len(nums)-1
        while start<=end and start>=0 and end<=len(nums)-1:
            mid=(start+end)/2
            if nums[mid]==target:
                start = mid
                end =  mid
                while start>0 and nums[start - 1] == nums[start]:
                    start = start - 1
                while end<len(nums)-1 and nums[end] == nums[end+1]:
                    end = end + 1
                return [start,end]
            else:
                if nums[mid]>target:
                    end=mid-1
                else:
                    start=start+1
        return [-1,-1]
s=Solution()
nums=[1]
target=1
print s.searchRange(nums,target)
