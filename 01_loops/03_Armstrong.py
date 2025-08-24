actual_num = 153
num = actual_num
nod = 0 
total = 0

while num > 0:
    num = num // 10
    nod += 1

num = actual_num

while num > 0:
    digit = num % 10
    total += pow(digit, nod)
    num = num // 10

if total == actual_num:
    print("it's an armstrong number")
else:
    print("it's not an armstrong number")