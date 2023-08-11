v = '()+-*/'
stack = []
s='(1+(4+5+2)-3)+(6+8)'
ans =''
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
for i in s:
    if i==' ':
        continue
    if i not in v:
        ans+=i
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
        
    else:
        while stack and precedence[i]<=precedence.get(stack[-1],0):
            ans+=stack.pop()
        stack.append(i)
while stack:
    ans+=stack.pop()
print(ans)



