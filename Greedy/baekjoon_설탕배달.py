# baekjoon
# 2839 설탕배달

sugar = int(input())            # 배달할 설탕 kg
count = 0                       # 봉지의 개수

while sugar >= 0:
    if sugar % 5 == 0:          # 5의 배수
       count += sugar // 5      # 5로 나눈 몫이 봉지의 개수
       print(count)
       break
    sugar -= 3                  # 5의 배수가 될 때까지 sugar에서 3을 빼준다
    count += 1                  # 빼줄때마다 봉지의 개수 +1
else:                           # 둘다 아닐 경우
    print(-1)                   # -1 출력