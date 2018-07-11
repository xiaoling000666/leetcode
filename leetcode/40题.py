class Solution(object):
    def combinationSum2(self, candidates, target):
        self.result=[]
        candidates.sort()
        start=0
        val=[]
        self.sum=0
        self.backdate(candidates, target, start,val)
        return self.sum
    def backdate(self,candidates,target,start,val):
        for i in range(start,len(candidates)):
            if target<0:
                break
            else:
                val.append(candidates[i])
                if target - candidates[i]==0:
                    if val not in self.result:
                        self.result.append(val[:])
                self.backdate(candidates, target-candidates[i],i+1, val)
                val.pop()
                self.sum=self.sum+1
                if(i < len(candidates)-1 & candidates[i]==candidates[i+1]):
                    break


candidates = [1,2,2,4]
target = 5
s=Solution()
print s.combinationSum2(candidates, target)

