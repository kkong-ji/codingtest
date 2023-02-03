# 백준 9375번
# 중복이 되면 안 되게 입을 수 있는 경우의 수는 다음과 같다.
# (의상 종류 1에서 선택 가능한 수 + 1) * (의상 종류 2에서 선택 가능한 수 + 1) * ... * (의상 종류 n에서 선택 가능한 수 + 1) - 1 (옷을 입지 않은 경우의 수)

testcase = int(input())

for i in range(testcase):
    map = {}
    answer = 1
    n = int(input())
    for j in range(n):
        a, b = input().split()
        if not b in map:            # b가 map에 없다면
            map[b] = 1              # b의 키값에 해당하는 value를 1
        else:                       # b가 map에 있다면
            map[b] += 1             # b의 키값에 해당하는 value를 1증가 (오픈 어드레싱 방식)
    for k in map.keys():            # key를 돌면서 answer에 key에 해당하는 (value + 1) 을 곱해줌 (의상의 종류에서 선택 가능한 수 + 1)
        answer = answer * (map[k]+1)
    print(answer-1)