# 문제: 첫째줄부터 N번째 줄까지 차례대로 별을 출력. 그러나, 가운데를 기준으로 대칭으로 출력하라.

n = int(input())

for i in range(n):
    for j in range(n-i-1):
        print(' ', end="")
    for j in range(2*i + 1):
        print('*', end="")
    print()