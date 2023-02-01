# baekjoon
# 1343 폴리오미노

board = input()

for i in range(0, len(board)):
    if 'XXXX' in board:                         # XXXX가 포함된 경우
        board = board.replace('XXXX', 'AAAA')   # replace 함수를 사용해서 바꿔줌

for i in range(0, len(board)):
    if 'XX' in board:                           # XX가 포함된 경우
        board = board.replace('XX', 'BB')

if 'X' in board:                                # 위에서도 걸러지지 못하고 X가 남을 경우
    board = "-1"                                # -1 출력

print(board)