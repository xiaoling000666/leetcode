class Solution(object):
    def multiply(self, num1, num2):
        sum=0
        for i in range(len(num1[0])):
            for j in range(len(num2[0])):
                sum=sum+10**((len(num2[0]))-j-1)*10**((len(num1[0]))-i-1)*int(num1[0][i])*int(num2[0][j])
        s=str(sum)
        return str(sum)