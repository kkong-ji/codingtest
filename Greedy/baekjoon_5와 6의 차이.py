# baekjoon
# 2864 5와 6의 차이

a, b = input().split()
min = int(a.replace('6', '5')) + int(b.replace('6', '5'))   # replace 함수 어떤 값을 찾아 그 값을 바꿔줌
max = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(min, max)