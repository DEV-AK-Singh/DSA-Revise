nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
lb = -1
target = 7
low = 0
high = len(nums)-1
while high >= low:
    mid = (high+low)//2
    if nums[mid] >= target:
        lb = mid
        high = mid - 1
    else:
        low = mid + 1
print(lb)