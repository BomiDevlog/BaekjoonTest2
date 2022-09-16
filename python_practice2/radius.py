# 으뜸 파이썬 챕터2 - 연습문제2.12~14

radius = 11
PI = 3.141592 # 반지름
print(f'''원의 반지름 = {radius},
원의 둘레 = {2*radius*PI},
원의 면적 = {radius*radius*PI}''')

r=int(input('원의 반지름을 입력하세요 :'))
print(f'원의 둘레 = {2*r*PI}, 원의 면적 = {r*r*PI}')

for i in range(2,11):
    print(f'{i}의 제곱근 = {i**(1/2)}')