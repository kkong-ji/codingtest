# 출력
print("Hello World!")

# 입력
print("1.정수 하나를 입력 받기")
num = int(input())
print(num)

print("\n2. 띄어쓰기로 숫자 두 개 입력 받기")
a, b = map(int, input().split())
print(a, b)

print("\n3. 리스트를 통해 정수 한 줄을 입력 받기")
num2 = list(map(int, input().split()))
print(num2)

print("\n4. 한 줄로 문자열 변수 여러 개를 입력 받기")
c, d = input().split()
print(c, d)

print("\n5. 문자열 여러 줄을 입력 받기")
str = [input() for i in range(3)]
print(str)

print("\n6. 한 줄에 띄어쓰기 없이 정수를 여러 개 받았을 때, 2차원 배열 형태로 출력하기")
arr = [list(map(int, input())) for i in range(4)]
print(arr)

print("\n7. 띄어쓰기가 있는 배열을 여러 개의 줄을 통해 입력 받을 때, 2차원 배열 형태로 출력하기")
arr2 = [list(map(int, input().split())) for i in range(3)]
print(arr2)



