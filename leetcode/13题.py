height=[0,2]
i=0
j=len(height)-1
max_s=0
while i!=j:
    if height[i]>height[j]:
        s=height[j]*(j-i)
        j-=1
        if s>max_s:
            max_s=s
    else:
        s=height[i]*(j-i)
        i+=1
        if s>max_s:
            max_s=s
print max_s


