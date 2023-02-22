N, M = map(int, input().split())
ball = []

for i in range(N):
    ball.append(i+1)

for j in range(M):
    A, B = map(int, input().split())
    ball[A-1], ball[B-1] = ball[B-1], ball[A-1]
print(*ball)



