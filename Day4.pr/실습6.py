a = input('문자열을 입력하세요')
dict_variable = {}
for s in a:
    n = 0
    for i in a: 
        if s in i: 
            n += 1
    dict_variable[s] = n

for w in dict_variable:
    print(w,dict_variable[w])