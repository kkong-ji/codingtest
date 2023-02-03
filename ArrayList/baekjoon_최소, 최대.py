# 백준 10818번
# 문제 : N개의 정수가 주어진다. 이때, 최댓값과 최솟값을 구하는 프로그램을 작성하시오.

N = int(input())
arr_list = list(map(int, input().split()))

max_num = arr_list[0]
min_num = arr_list[0]

for num in arr_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(min_num, max_num)
