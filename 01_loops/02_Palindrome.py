actual_num = 1221
num = actual_num
rev = 0 
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if actual_num == rev:
    print(f"Number is a PALINDROME as {actual_num} and {rev} are equal.")
else:
    print(f"Number is NOT a PALINDROME as {actual_num} and {rev} are not equal.")