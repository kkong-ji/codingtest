# baekjoon
# 2847 게임을 만든 동준이

n = int(input())
point = []
temp_point = []
minus_point = 0

for i in range(0, n):
    k = int(input())
    point.append(k)

    last_point = point[-1]

if point[-2] >= last_point:
    temp_point.append(last_point - (n-1))

    for j in range(1, n):
        temp_point.append(temp_point[0]+j)

    for k in range(0, n):
        minus_point += point[k] - temp_point[k]

else:
    temp_point.append(last_point - n)

    for j in range(1, n):
        temp_point.append(temp_point[0] + j)
        print(temp_point)
    for k in range(0, n):
        minus_point += point[k] - temp_point[k]


print(minus_point)

