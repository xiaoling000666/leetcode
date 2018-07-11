class Solution(object):
    def letterCombinations(self, digits):
        button=['','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res=[]
        global word
        word=''
        if digits=='':
            return []
        else:
            def dfs(cir):
                global word
                if cir>=len(digits):
                    res.append(word)
                else:
                    for x in button[int(digits[cir])]:
                        word=word+x
                        dfs(cir+1)
                        word=word[:-1]

a=Solution()
digits='234'
a.letterCombinations(digits)
