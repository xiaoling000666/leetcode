class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        solution=[]
        k=0
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                two_sum=target-nums[i]-nums[j]
                m = j+1
                n = len(nums) - 1
                while m<n:
                    if nums[m]+nums[n]>two_sum:
                        n-=1
                    elif nums[m]+nums[n]<two_sum:
                        m+=1
                    else:
                        solution.append([nums[i],nums[j],nums[m],nums[n]])
                        if k >= 1 and k <=len(solution) and solution[k] == solution[k - 1]:
                            solution.pop()
                            k-=1
                        k=k+1
                        n=n-1
                        m=m+1
        new_solution = []
        for i in solution:
            if i not in new_solution:
                new_solution.append(i)
        return new_solution
nums=[1,0,-1,0,-2,2]
target=0
Solution.fourSum(nums,target)

