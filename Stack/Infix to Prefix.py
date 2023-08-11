v = '()+-*/'
stack = []
s="(1+(4+5+2)-3)+(6+8)"
n=''
for i in range(len(s)):
        if s[i] in '(':
            n+=  ')'
        elif s[i] in ')':
            n+= '('
        else:n+=s[i]
ans =''
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
print(s)
for i in n[::-1]:
    
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
print(ans[::-1])
