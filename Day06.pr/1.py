a = input('문자열을 입력하세요')
n = 0

for i in a:
    if i == 'e':
        break
    elif 'e' not in a:
        n = -1
        break
    n += 1
print(n)