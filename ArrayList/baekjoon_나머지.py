# 백준 3052번

N = []
divide = []
answer = []

for i in range(10):
    N.append(int(input()))
    divide.append(N[i]%42)

for j in divide:
    if j not in answer:         # 중복 제거
        answer.append(j)

print(len(answer))