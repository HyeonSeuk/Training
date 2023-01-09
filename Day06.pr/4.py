a = input('문자열을 입력하세요').split()
n = 0
for i in a[0]:
    if i == a[1]:
        n += 1
print(n)