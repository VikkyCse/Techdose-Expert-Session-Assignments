arr = [10, 4, 2, 20, 40, 12, 30]


s = []
ans = []
for i in arr:
    print(s,ans,end = "\n")
    while s and s[-1] < i:
        s.pop()
    s.append(i)
    if len(s)<=1:
        ans.append(-1)
    
    else:
        ans.append(s[-2])
    
print(ans)



