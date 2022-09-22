# https://www.acmicpc.net/problem/2839 설탕배달
# https://www.acmicpc.net/problemset?sort=ac_desc&algo=33 그리드알고리즘
# 신입사원 https://www.acmicpc.net/problem/1946

# [백준/파이썬] 2839번 설탕 배달
# 문제 핵심 요약 : 그리드 알고리즘
# https://blog.naver.com/deu03216/222810264789

# 11의 경우. 무조건 큰수부터 접근하면 안됨. 5나누기로 개수 측정 불가.

# 5씩 빼서 횟수 카운트. 전체 N에서 5씩 빠지는 것을 개수 측면에서도 고려해야함
# 5의 배수가 아니면서 3의 배수(나머지)인 경우는 나누기3으로 개수측정

N = int(input()) # 설탕배달 봉지 개수

count = N//5
result = -1

for i in range(count,-1,-1): # 봉지 개수를 0까지, 1개씩 숫자 줄임
    if (N-5*i)%3 == 0:
        result = i + (N-5*i)//3
        break

print(result)

# 5씩 빼면서 횟수(result)를 센다
# 3의 배수인 경우는 나누기3으로 횟수를 센다
# (예시인 6,9 혹은 11을 참고함) 