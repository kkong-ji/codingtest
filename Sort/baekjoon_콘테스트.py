# 백준 5576번
w = []
k = []
w_score = 0
k_score = 0

for i in range(0, 10):
    w.append(int(input()))
    w.sort(reverse=True)

for j in range(10, 20):
    k.append(int(input()))
    k.sort(reverse=True)

print(w[0]+w[1]+w[2], k[0]+k[1]+k[2], end=" ")

