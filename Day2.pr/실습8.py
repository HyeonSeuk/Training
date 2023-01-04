a = int(input('첫 번째 숫자를 입력하세요'))
b = int(input('두 번째 숫자를 입력하세요'))

if a > b:
    for i in range(a-1, b, -1):
        print(i, end=" ")
elif b > a:
    for i in range(b-1, a, -1):
        print(i, end=" ")
else:
    print(False)