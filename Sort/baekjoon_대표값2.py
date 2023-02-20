N = []

for i in range(5):
    N += map(int, input().split())
    average = sum(N) / 5
N.sort()

print(int(average))
print(N[2])