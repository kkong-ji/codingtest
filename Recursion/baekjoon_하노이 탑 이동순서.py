# 백준 11729번

def hanoi(num, start, to, end):                 # 원판 num과 원판의 장대의 시작 위치 = start, 중간 위치 = to, 마지막 위치 = end
    if num == 1:
        print(start, end)
    else:
        hanoi(num-1, start, end, to)
        print(start, end)
        hanoi(num-1, to, start, end)

num = int(input())
print(2**num - 1)
hanoi(num, 1, 2, 3)