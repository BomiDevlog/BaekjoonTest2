# https://www.acmicpc.net/problem/11726
# [백준] 11726번 2×n 타일링  =>  2(세로) x n (가로)
# 문제 핵심 요약 : DP

# 2 x n 의 입력값 n
n = int(input())

# dp 리스트 생성 
dp = [0] * 1001 

# 경우의 수: 2x1 => 1가지. 2x2 => 2가지
dp[1], dp[2] = 1, 2

# 2x3 이후의 규칙을 점화식으로 형성
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
