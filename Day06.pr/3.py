# a = input('문자열을 입력하세요')
# t = 'e'

# a = ''.join( x for x in a if x not in t)
# print(a)

a = input('문자열을 입력하세요')

for i in a:
    if i == 'e':
        continue
    print(i, end='')