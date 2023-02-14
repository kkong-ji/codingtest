# 백준 20291번

N = int(input())

file_count = {}
d = {}
id = []

for _ in range(N):
    a, b = input().strip().split('.')
    if b in d:
        d[b] += 1
    else:
        d[b] = 1
        id.append(b)

id.sort()
for name in id:
    print(name, d[name])