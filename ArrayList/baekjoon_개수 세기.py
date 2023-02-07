# 백준 10807번

N = int(input())
arr = list(map(int, input().split()))
v = int(input())
answer = 0

for i in arr:
    if v == i:
        answer += 1
print(answer)