a = input('문자열을 입력하세요')
dict = {}

for i in a:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for key in dict:
    print(key, dict[key])