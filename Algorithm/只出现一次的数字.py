class Solution(object):
    def singleNumber(self, nums):
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 0
            else:
                dict[nums[i]] += 1
        for i in dict:
            if dict[i] == 0:
                return i
s = Solution()
nums = [4,1,2,1,2]
print(s.singleNumber(nums))
