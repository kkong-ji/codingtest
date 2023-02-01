# baekjoon
# 1789 수들의 합

s = int(input())

sum = 0
i = 1

while sum <= s:
    i += 1
    sum += i
    if sum >= s:
        i -= 1
        break
print(i)

