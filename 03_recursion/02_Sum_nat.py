# def sum_nat(n, sum=0):
#     if n==0:
#         print(sum)
#         return
#     sum = sum + n
#     sum_nat(n-1, sum)
# sum_nat(5)

def sum_nat(n):
    if n == 1:
        return 1
    return n + sum_nat(n-1)
print(sum_nat(5))