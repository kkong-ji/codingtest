# 배열에서 인덱스로 값 뽑아서 더하기

arr = [7, 3, 2, 9]

# def sum(arr):
#     last = arr.pop()
#     print("arr =>", arr)
#     print("last =>", last)
#     result = arr[0] + arr[1] + arr[2] + last
#     return result
#
# result = sum(arr)
# print("result =>", result)


# 만약 pop으로 배열의 마지막 수를 계속해서 뽑아내어 더한다면?

def sum(arr):
    last = arr.pop()
    result = last
    last = arr.pop()
    result = result + last
    last = arr.pop()
    result = result + last
    last = arr.pop()
    result = result + last
    return result

result = sum(arr)
print("result =>", result)

# 위 함수를 재귀호출로 나타내보자

