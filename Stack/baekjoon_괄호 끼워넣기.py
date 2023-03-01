# 백준 11899번 괄호 끼워넣기

n = input()
stack = []

for i in range(len(n)):
    if n[i] == '(':
        stack.append(n[i])
    elif n[i] == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(n[i])
print(len(stack))
