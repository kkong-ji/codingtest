# 백준 10870번

def fibo(n):
    if n<= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

N = int(input())
print(fibo(N))
