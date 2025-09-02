def int_to_bin(num):
    result = ""
    while num > 0:
        if num%2 == 1:
            result += "1"
        else:
            result += "0"
        num = num//2
    result = result[::-1]
    return result

# reverse a number
# a = 5
# b = 10
# print(a,b)
# a = a^b 
# b = a^b
# a = a^b 
# print(a,b)


# # check if ith bit set or not

# # left shift
# num = 13 # 1101 
# i = 1
# res = num & (1 << i)
# print(True if res!=0 else False)

# # right shift
# num = 13 # 1101 
# i = 0
# res = (num >> i) & 1
# print(True if res==1 else False)

# # set ith bit
# n = 9
# i = 4 
# res = (1 << i) | n
# print(f"{int_to_bin(n)} -> {int_to_bin(res)}")

# # # clear ith bit
# n = 13
# i = 0
# res = (n) & (~(1 << i))
# print(f"{int_to_bin(n)} -> {int_to_bin(res)}")

# # toggle ith bit
# n = 13 
# i = 2 # 1101 -> 1001
# # i = 1 # 1101 -> 1111
# res = n ^ (1 << i)
# print(f"{int_to_bin(n)} -> {int_to_bin(res)}")

# # remove last set bit [right most]
# n = 84
# res = n & (n-1)
# print(f"{int_to_bin(n)} -> {int_to_bin(res)}")

# # check power of 2
# n = 64
# res = n & (n-1)
# print(True if res == 0 else False) 