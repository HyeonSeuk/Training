dict_variable = {
    '이름' : input('이름을 입력하시오'),
    '전화번호' : input('전화번호를 입력하세요'),
    '거주지' : input('거주지를 입력하세요')
}
print(dict_variable)

for key in dict_variable:
    print(key,':', dict_variable[key])
