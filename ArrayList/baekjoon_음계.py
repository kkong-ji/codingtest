# 백준 2920번

Num_arr = list(map(int, input().split()))
ascNum = []
desNum = []

for i in range(8):
    ascNum.append(i+1)
    desNum.append(i+1)
    desNum.sort(reverse=True)


if Num_arr == ascNum:
    print("ascending")
elif Num_arr == desNum:
    print("descending")
else:
    print("mixed")