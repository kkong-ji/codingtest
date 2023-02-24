# 최대 공약수의 4가지 정의

# 1. gcd(a, a) = a
# 두 수가 같으면 최대 공약수는 a

# 2. gcd(a, b) = gcd(a, a + b)
# 두 수가 다를 떄 두수의 최대공약수와 두 수 중 작은 수에 b를 더한 수와 작은 수의 최대 공약수는 같다

# 3. a > b => gcd(a, b) = gcd(a - b, b)
# b 가 a 보다 작은 경우 두 수 a, b의 최대공약수와 큰 수인 a에서 b를 뺀 수와 b의 최대 공약수는 같다

# 4. gcd(a, b) = gcd(b, a)
# a, b의 최대공약수는 b, a의 최대공약수와 같다

def gcd(first, second):
    print(first, second)
    if first == second:                 # 1번 정의
        return first
    if first > second:                  # 3번 정의
        return gcd(first - second, second)
    if first < second:                  # 3번 정의 응용
        return gcd(first, second - first)
    return 1

print("result=>", gcd(196, 42))