# 백준 3003번

N = list(map(int, input().split()))
chessArr = [1, 1, 2, 2, 2, 8]
answerArr = []

for i in range(len(N)):
    answerArr = chessArr[i] - N[i]
    print(answerArr)