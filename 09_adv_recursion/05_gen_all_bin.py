n = 5
res = []

def gen_all_bin(index, bin, flag, res):
    if index >= len(bin): 
        res.append("".join(bin))
        return 
    bin[index] = "0"
    gen_all_bin(index+1, bin, True, res)
    if flag:
        bin[index] = "1"
        gen_all_bin(index+1, bin, False, res)
        bin[index] = "0"
    
gen_all_bin(0, ["0"]*n, True, res)

print(res)