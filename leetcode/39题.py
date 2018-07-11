class Solution(object):
    def combinationSum(self, candidates, target):
        candidates = list(set(candidates))
        sorted(candidates)
        self.result= []
        start=0
        self.backtrack(candidates, target,start,[])
        return self.result
    def backtrack(self,candidates,target,start,val):
        if target == 0:
            self.result.append(val[:])
        for i in range(start,len(candidates)):
            if target>0:
                val.append(candidates[i])
            else:
                break
            self.backtrack(candidates, target - candidates[i], i,val)
            val.pop()

candidates=[2,3,6,7]
target=7
s=Solution()
print s.combinationSum(candidates, target)

