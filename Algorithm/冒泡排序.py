class Solution():
    def Bubble_sort(self, list):
        for i in range(len(list) - 1, 0, -1):
            for j in range(i):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
        return list

s=Solution()
list=[49,38,65,97,76,13,27,49]
print(s.Bubble_sort(list))
