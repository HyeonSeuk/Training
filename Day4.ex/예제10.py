n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0:
        total += number * 2
    elif number % 2 == 1:
        total += number + 1 * 3

print(total) # 100

# 짝수면 그 수 두배 더하고 홀수면 그수+3해서 더하는 식
# number  0 1 2 3  4  5  6  7  8  9  10
# total   0 4 8 14 22 30 42 52 68 80 100