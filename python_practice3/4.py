# 연습문제 3.2~3.3

name = input('이름을 입력하시오 :')
age = int(input('나이를 입력하시오 :'))
height = int(input('키를 입력하시오 (단위: cm) :'))

if age >= 19 and height >= 150 :
    print(f'{name} 님은 입장 가능합니다')
else :
    print(f'{name} 님은 입장할 수 없습니다')

