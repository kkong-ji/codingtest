# baekjoon
# 16435 스네이크 버드

n, L = input().split()
n = int(n)
L = int(n)

fruit = list(map(int, input().split(" ")))
snake_length = 0

for i in fruit:
    if i==L:
        snake_length = i + 1
        print(snake_length)
    while snake_length == i:
       snake_length += 1
       if snake_length != i:
           print(snake_length)

