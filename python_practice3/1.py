# 1~100까지 정수합 -sum이용
print(sum(range(1,101)))

# 문자열 순회
for ch in 'Hello':
    print(ch, end=" ")

print()

# 상향식 문제풀이
n =5
for i in range(n):
    print(n-(i+1), end=' ')

# 4 3 2 1 0
print()


for i in range(n):
    for j in range(n-(i+1)): # 공백 4 3 2 1
        print(' ', end='')
    for k in range(2*i + 1): # 1,3,5,7,9 개 프린트
        print('*', end='')
    print()
