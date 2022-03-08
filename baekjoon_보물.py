# baekjoon
# 1026 보물

n = int(input())    # 길이가 n
a = list(map(int, input().split()))     # a의 값을 map으로 선언
b = list(map(int, input().split()))     # b의 값을 map으로 선언
a.sort()                                # a를 오름차순 sorting
b.sort(reverse=True)                    # b를 내림차순 sorting

s = 0               # 최솟값
for i in range(0, n):
    s += a[i] * b[i]
print(s)

