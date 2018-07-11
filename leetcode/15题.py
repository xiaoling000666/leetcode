class Solution(object):
    def threeSum(self, s):
        s.sort()
        solution=[]
        for i in range(len(s)):
            if s[i]==s[i-1] and i>0:
                i+=1
            else:
                j=len(s)-1
                k=i+1
                two_sum = 0 - s[i]
                while k<j:
                    if s[k] + s[j] < two_sum:
                        k += 1
                    elif s[k] + s[j] > two_sum:
                        j -= 1
                    else:
                        solution.append([s[i], s[k], s[j]])
                        k += 1
                        j -= 1
                        while s[k]==s[k-1] and k<j:
                            k+=1
                        while s[j]==s[j+1] and k<j:
                            j-=1
        return solution
a=Solution()
s=[0,0,0,0,0]
a.threeSum(s)












