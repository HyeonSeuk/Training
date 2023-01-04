a = int(input('숫자를 입력하세요'))

if a < 1:
    print(False)
else:
    for i in range(1,a,2):
        print(i)