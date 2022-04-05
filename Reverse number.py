number = int(input('please enter your number: '))
reverse_num = 0
while number > 0:
    temp = number % 10
    reverse_num = reverse_num * 10 + temp
    number = number // 10
print(reverse_num)