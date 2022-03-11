# baekjoon
# 11399 ATM

N = int(input())

time = 0
each_time = list()                              # 각 사람들의 사용 시간을 리스트로 저장
people = list(map(int, input().split()))

people.sort()                                   # 오름차순 정렬

for user in people:                             # people을 for문 돌면서
  time += user                                  # time에는 각 사용자들의 값을 더하면서 저장
  each_time.append(time)                        # 만들어둔 리스트에 time을 더하면서 저장

result = sum(each_time)
print(result)


