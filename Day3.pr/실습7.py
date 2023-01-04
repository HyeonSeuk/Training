number_list = [1, 2, 3, 4, 5]
a = 99999999
for element in number_list:
    if element < a:
        a = element
print(a)
