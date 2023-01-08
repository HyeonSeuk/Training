name = input("이름을 입력하세요 > ")
phone_number = input("전화번호를 입력하세요 > ")
email = input("이메일을 입력하세요 > ")
residence = input("거주지를 입력하세요 > ")

dict_variable = {
    name: {
        "전화번호": phone_number,
        "이메일": email,
        "거주지": residence,
    }
}
print(dict_variable)
