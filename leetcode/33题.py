class Solution(object):
    def search(self, nums, target):
        start=0
        end=len(nums)-1
        if len(nums)==1 and nums[0]==target:
            return 0
        else:
            while start<=end:
                mid = (start + end) / 2
                if nums[mid]==target:
                    return mid
                else:
                    if nums[mid]<nums[end]:
                        if target<=nums[end] and target>nums[mid]:
                            start=mid+1
                        else:
                            end=mid-1
                    else:
                        if target>=nums[start] and target<nums[mid]:
                            end=mid-1
                        else:
                            start=mid+1
            return -1
a=Solution()
nums=[3,5,1]
target=3
print a.search(nums,target)
