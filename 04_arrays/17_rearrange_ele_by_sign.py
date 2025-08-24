nums = [5,10,-3,-1,-10,6]
res = [0]*len(nums)
p=0
n=1
for ele in nums:
    if ele < 0:
        res[n] = ele
        n+=2
    elif ele > 0:
        res[p] = ele 
        p+=2
print(res)

        
        