# 백준 10799 쇠막대기

n = (input())
stack = []
stick = 0

for i in range(len(n)):
    if n[i] == '(':
         stack.append(n[i])
    else:                           # n[i] 가 ')' 일때
        if n[i-1] == '(':           # n[i-1] 가 '(' 이면
            stack.pop()             # 스택의 맨 위의 원소를 삭제
            stick += len(stack)
        else:
            stack.pop()
            stick += 1
print(stick)

