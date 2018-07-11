#-*-coding:utf-8-*-
def jiansheng(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    list = [0]*(n+1)
    list[1] = 1
    list[2] = 2
    list[3] = 3
    for i in range(3, n+1):
        for j in range(1, i/2+1):
            mult = list[j]*list[i-j]
            if mult > list[i]:
                list[i] = mult
    return list[n]
print(jiansheng(8))