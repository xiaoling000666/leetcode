class Solution():
    def string_decoding(self,A):
        list=[0]*len(str(A))
        list[0] = 1
        list[1] = 1
        if len(list) == 1:
            return list[0]
        tmp = str(A)[0] + str(A)[1]
        if len(list) == 2:
            if int(tmp) < 26:
                list[1] = 2
            else:
                list[1] = 1
            return list[1]
        if int(tmp) < 26:
            list[1] = 2
        for i in range(2, len(str(A))):
            if int(str(A)[i]) >= 0 and int(str(A)[i]) <= 9:
                tmp = str(A)[i-1]+str(A)[i]
                if int(tmp) < 26:
                    list[i] = list[i - 1] + list[i - 2]
                else:
                    list[i]=list[i-1]
        return list

s = Solution()
#A = 31
A = 1231725
print(s.string_decoding(A))


