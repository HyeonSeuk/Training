a = int(input('첫 번째 정수를 입력하세요'))
b = int(input('두 번째 정수를 입력하세요'))


if b > a:
    for i in range(a+1, b):
        print(i)
    
elif a > b:
    for i in range(b+1, a):
        print(i)
else:
    print('False')
    
    