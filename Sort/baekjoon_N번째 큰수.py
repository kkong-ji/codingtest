# 백준 2693번

N = int(input())

for _ in range(N):
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    print(nums[2])