a = int(input('정수를 입력하세요'))
result = ""

if a > 100:
    result = '에러'
elif 100 > a >= 60:
    result = '합격'
elif 60 > a >= 0:
    result = '불합격'
else:
    result = '에러'
    
print(result)