# 백준 1541번

equtation = input().split('-')
answer = 0

for i in equtation[0].split('+'):
    answer += int(i)                # 마이너스가 나오기 이전의 수는 answer에 모든 수를 더한다.

for i in equtation[1:]:             # 마이너스가 나온 이후의 수는 answer에 모든 수를 뺀다.
    for j in i.split('+'):
        answer -= int(j)

print(answer)