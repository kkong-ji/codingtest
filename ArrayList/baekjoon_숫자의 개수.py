# 백준 2577번

multiple = 0
answer = []
numCount = []

A = int(input())
B = int(input())
C = int(input())

multiple = A*B*C

for i in str(multiple):
    answer.append(i)

for j in range(10):
    numCount.append(0)

for k in range(len(answer)):
    if answer[k] == '0':
        numCount[0] += 1
    if answer[k] == '1':
        numCount[1] += 1
    if answer[k] == '2':
        numCount[2] += 1
    if answer[k] == '3':
        numCount[3] += 1
    if answer[k] == '4':
        numCount[4] += 1
    if answer[k] == '5':
        numCount[5] += 1
    if answer[k] == '6':
        numCount[6] += 1
    if answer[k] == '7':
        numCount[7] += 1
    if answer[k] == '8':
        numCount[8] += 1
    if answer[k] == '9':
        numCount[9] += 1

for l in numCount:
    print(l)