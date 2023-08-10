arr = [1, 6, 4, 10, 2, 5]


s = []
ans = []
for i in arr:
    print(s,ans,end = "\n")
    while s and s[-1] > i:
        s.pop()
    s.append(i)
    if len(s)<=1:
        ans.append(-1)
    
    else:
        ans.append(s[-2])
    
print(ans)




