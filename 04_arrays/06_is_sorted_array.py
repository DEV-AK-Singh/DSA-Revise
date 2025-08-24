# nums = [55,32,-97,99,3,67]
nums = [5,32,97,99,322,672]
flag = True
for i in range(1,len(nums)):
    if nums[i-1] > nums[i]:
        flag = False
        break
print(flag)