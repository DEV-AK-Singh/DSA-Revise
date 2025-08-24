num = 102000
count = 0
flag = False
while num > 0:
    digit = num % 10
    if digit != 0:
        flag = True
    if flag:
        print(digit, sep='', end='') 
    num = num // 10
    count += 1
print("\nNumber of digits:", count)
