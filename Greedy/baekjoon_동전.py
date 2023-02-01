# baekjoon
# 11047 동전 0

n, k = map(int, input().split())                # n = 동전 종류, k = 주어진 금액
                                                # ex. n = [1, 5, 10] , k = 300원
coin_list = []                                  # coin_list 리스트 선언
coin_list = [int(input()) for i in range(n)]    # coin_list를 for문 돌면서 input

coin_list.sort(reverse=True)                    # 내림차순 정렬

count = 0
for j in coin_list:
    count += k // j                             # count에 주어진 금액을 coin_list로 나누었을 때 몫의 값을 더함
    k = k % j                                   # k에는 j로 나누고 나머지의 값을 대입한다.
print(count)




