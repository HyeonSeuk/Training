s = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
n = 0
for i in input('문자를 입력하시오'):
    if i in s:
        n += 1
print(n)