# 백준 10773번 제로

n = int(input())
stack = []

for i in range(n):
    A = int(input())
    if A == 0:
        stack.pop()
    else:
        stack.append(A)

print(sum(stack))