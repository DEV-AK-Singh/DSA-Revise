n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
nm = [10, 111, 67, 2]

max_ele = max(n)
freq_n = [0 for i in range(0, max_ele+1)] 

for ele in n:
    freq_n[ele] += 1 

for ele in nm:
    if ele < 1 or ele > max_ele:
        print(0)
    else:
        print(freq_n[ele])