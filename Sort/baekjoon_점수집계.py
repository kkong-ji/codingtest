# 백준 9076번

N = int(input())

for i in range(N):
    score = list(map(int, input().split()))
    score.sort(reverse=True)
    score.remove(score[0])
    score.remove(score[3])

    if score[0] - score[2] >= 4:
        print("KIN")
    else:
        result = sum(score)
        print(result)