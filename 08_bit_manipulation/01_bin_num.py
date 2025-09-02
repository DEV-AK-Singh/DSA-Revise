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

def bin_to_int(num):
    index = len(num) - 1
    dec_num = 0
    power = 0
    while index >= 0:
        dec_num += int(num[index]) * pow(2, power)
        index -= 1
        power += 1
    return dec_num

print(int_to_bin(13001))
# print(bin_to_int("1101"))

def and_opr(bin1, bin2):
    dec1 = bin_to_int(bin1)
    dec2 = bin_to_int(bin2)
    res = dec1 & dec2
    return int_to_bin(res)

# print(and_opr("1101","1001"))

# def or_opr(bin1, bin2):
#     dec1 = bin_to_int(bin1)
#     dec2 = bin_to_int(bin2)
#     res = dec1 | dec2
#     return int_to_bin(res)

# print(or_opr("1101","1010"))

def xor_opr(bin1, bin2):
    dec1 = bin_to_int(bin1)
    dec2 = bin_to_int(bin2)
    res = dec1 ^ dec2
    return int_to_bin(res)

print(xor_opr("1101","1010"))

