arr = [13 , 7, 6 , 12]



s = []
ans = []
for i in arr[::-1]:
    print(s,ans,end = "\n")
    while s and s[-1] > i:
        s.pop()
    s.append(i)
    if len(s)<=1:
        ans.append(-1)
    
    else:
        ans.append(s[-2])
    
print(ans[::-1])
