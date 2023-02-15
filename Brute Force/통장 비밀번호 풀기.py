# 문제 : 4자리로 되어있는 통장 비밀번호를 알아내는 알고리즘을 만들어 보자.
# 0000부터 9999까지 무차별 대입을 하다가 입력받은 pw와 일치하는 경우
# True를 리턴하는 로직을 구현
# Hint : for 문을 4개 사용하자

def solution(pw):
    # h i j k
    for h in range(0, 10):
        for i in range(0, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    made_pw = f'{h}{i}{j}{k}'
                    # 만들어진 pw와 입력받은 pw 비교
                    if str(pw) == made_pw:
                        print(made_pw)
                        return True
print(solution(6697))