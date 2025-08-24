nums=[1,0,2,3,4,0,0,3,5,1]

n=len(nums)

for i in range(0,n-1):
    if nums[i] == 0:
        j = i+1
        while j<n:
            if nums[j]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                break
            j+=1

print(nums)