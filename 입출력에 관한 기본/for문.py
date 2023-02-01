# 문제: 첫째줄부터 N번째 줄까지 차례대로 별을 출력하라.
n = int(input())

for i in range(n):
    print("*" * (i+1))
