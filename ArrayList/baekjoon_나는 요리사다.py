# 백준 2953번

human = [list(map(int, input().split())) for i in range(5)]     # 각 참가자들의 점수를 2차원 배열 형태로 입력 받음
humanScore = [0] * 5                                            # 참가자들의 총합 점수를 저장하기 위한 배열 생성
score = 0                                                       # 최대 점수를 저장하기 위한 변수 생성
for i in range(5):                                              # 0부터 4까지 for문을 탐색해 참가자들을 순회
    sum = 0                                                     # 참가자의 점수를 저장하기 위한 변수 sum
    for j in range(4):                                          # 4번의 평가를 받았으므로 0~3까지 for문 실행
        sum += human[i][j]                                      # sum에 참가자가 받은 점수를 더해줌
    humanScore[i] = sum                                         # 해당 참가자의 총 점수는 sum에 저장
    score=max(score, sum)                                       # 점수의 최댓값을 score에 저장

for i in range(5):                                              # 참가자의 총 점수가 최대점수(score)라면
    if humanScore[i] == score:                                  # 참가자번호(i+1)과 최대점수를 출력하고 for문 탈출
        print(i+1, score)
        break
