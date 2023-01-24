a = int(input('정수를 입력하세요'))
n = 0

if n < 0:
    print(-1)
else:
    while a > 0:
        n += a % 10
        a = a//10
    print(n)