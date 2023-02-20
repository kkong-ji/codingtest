# 백준 2798번

N, M = map(int, input().split(" "))
card = []
blackjack = 0
combi = []
card += map(int, input().split(" "))

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):

            if card[i] + card[j] + card[k] == M:
                blackjack = card[i] + card[j] + card[k]
                combi.append(blackjack)
            if card[i] + card[j] + card[k] != M and card[i] + card[j] + card[k] < M:
                blackjack = card[i] + card[j] + card[k]
                combi.append(blackjack)
print(max(combi))



