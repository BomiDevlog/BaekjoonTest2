# 으뜸 파이썬 챕터2 - 연습문제2.17

for i in range(0,10):
    print(2 << i, end = ' ')


print()

# 으뜸 파이썬 챕터2 - 연습문제2.18

a = int(input('정수를 입력하세요 : '))
print('이 수가 짝수인가요?', end=" ")
if a%2 == 0:
    print ('True')
else :
    print('False')


print()   

# 으뜸 파이썬 챕터2 - 연습문제2.19

a = int(input('정수를 입력하세요 : '))
print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?', end=" ")
if a%2 == 0 and 0<=a<=100 :
    print ('True')
else :
    print('False')