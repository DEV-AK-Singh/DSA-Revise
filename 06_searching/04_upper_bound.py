nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
up = len(nums)
target = 9
low = 0
high = len(nums)-1
while high >= low:
    mid = (high+low)//2
    if nums[mid] > target:
        up = mid
        high = mid - 1
    else:
        low = mid + 1
print(up)