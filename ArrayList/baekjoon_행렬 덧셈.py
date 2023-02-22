N, M = map(int, input().split(" "))

A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(M)]

def solution(A, B):
    answer = []
    for i in range(len(A)):
        tmp = []
        for j in range(len(A[0])):
            tmp.append(A[i][j] + B[i][j])
        answer.append(tmp)
    return answer