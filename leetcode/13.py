class Solution(object):
    def intToRoman(self, num):
        dic1=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        dic2=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        for i in range(len(dic1)):
                while num>=dic2[i]:
                        num=num-dic2[i]
                        print(dic1[i])
s=Solution()
num=3
s.intToRoman(num)
