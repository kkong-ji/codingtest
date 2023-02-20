# 백준 11651번

N = int(input())
num = []

for _ in range(N):
    X, Y = map(int, input().split())
    num.append([X, Y])

num.sort(key=lambda x: (x[1], x[0]))

for i in num:
    print(i[0], i[1])