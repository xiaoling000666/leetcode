class Solution(object):
    def longestCommonPrefix(self, strs):
        list=strs
        list_length=[]
        list_number=''
        if list==[]:
            return  list_number
        else:
            for i in range(len(list)):
                list_length.append(len(list[i]))
            list_shortlength=min(list_length)
            for i in range(list_shortlength):
                k=1
                for j in range(len(list)-1):
                    if list[j][i]==list[j+1][i]:
                        k=k+1
                if k==len(list):
                    list_number=list_number+list[0][i]
                else:
                    break
            return list_number
strs=['leets','leetcode','leet','leeds']
s=Solution()
s.longestCommonPrefix(strs)













