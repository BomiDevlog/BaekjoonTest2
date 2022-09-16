st= 'Programming'

# 자음이 나타나는 동안만 출력하는 기능
for ch in st:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        break
    print(ch, end=' ')

print('(The end)')

# 자음이 나타날 때만 출력하는 기능
for ch in st:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        continue
    print(ch, end=' ')

print('(The end)')

# 가위 바위 보
selected = None
while selected not in ['가위', '바위', '보']: # 없으면 다시 물어본다
    selected = input('가위, 바위, 보 중에 선택하세요 : ')

print('선택한 값은', selected)

