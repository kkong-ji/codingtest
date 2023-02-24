# 1부터 100까지 출력하는 함수
# 재귀함수는 1. 파라미터, 2. 탈출 조건이 꼭 들어가야 한다

def print1To100(num):
    print(num)
    if num <= 100:
        print(num)
        print1To100(num+1)

# 1. 시작하는 값 : print1To100(1)
# 2. 변화는 어떻게 줄 것인지 : printTo100(num + 1)
# 3. 언제 끝낼 것인지 : if <= 100:

print1To100(1)

