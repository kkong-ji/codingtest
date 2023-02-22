N, M = map(int, input().split(" "))
basket = []
ballNum = []

for i in range(N):
    ballNum.append(0)

for j in range(M):
    basket = (list(map(int, input().split())))
    for k in range(basket[0]-1, basket[1]):
        ballNum[k] = basket[2]
        if basket[0] == basket[1]:
            ballNum[basket[1]-1] = basket[2]
print(*ballNum)
