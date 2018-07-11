n = 3
list =[0,0,0]
visit =[0,0,0]
def dfs(k):
    if k == n:
        print(list)
        return
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            list[k-1] = i+1
            dfs(k+1)
            visit[i] = 0
print(dfs(0))

