# 백준 1476번

E, S, M = map(int, input().split(" "))

year = 1

# 세 수의 나머지가 모두 0이 되는 연도
while True:
    if (year-E) % 15 == 0 and (year-S) % 28 == 0 and (year-M) % 19 == 0:
        break
    year += 1

# 연도 출력
print(year)
