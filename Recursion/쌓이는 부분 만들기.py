# 무한히 호출되는 에러를 해결하기 전에 재귀가 끝났을 때 결과를 리턴하려면
# 재귀가 한 바퀴 돌 때마다 쌓이는 변수가 있어야함

# arr = [7, 3, 2, 9]
# def sum(arr, accu):
#     print(arr, accu)
#     last = arr.pop()
#     result = last
#     return sum(arr, accu)
#
# result = sum(arr, 0)
# print("result=>", result)

# 탈출 조건 적용하기
# arr = [7, 3, 2, 9]
# def sum(arr, accu):
#     print(arr, accu)
#     if(len(arr) == 0):
#         return accu
#
#     last = arr.pop()
#     result = last
#     return sum(arr, accu)
#
# result = sum(arr, 0)
# print(result)

# 하나씩 뽑는 로직은 동작하니 이제 accu의 값이 쌓이도록 로직을 추가해보자
# arr = [7, 3, 2, 9]
# def sum(arr, accu):
#     print(arr, accu)
#
#     if(len(arr) == 0):
#         return accu
#
#     last = arr.pop()
#     result = last
#
#     return sum(arr, accu+result)
#
# result = sum(arr, 0)
# print(result)

# 소스 코드를 깔끔하게 정리하기
arr = [7, 3, 2, 9]
def sum(arr, accu):
    if(len(arr) == 0): return accu
    return sum(arr, accu + arr.pop())

print("result=>", sum(arr, 0))
