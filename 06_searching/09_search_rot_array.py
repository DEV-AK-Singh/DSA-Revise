nums = [17,18,19,20,1,3,4,5,7,8,10,11,13,14,16]
target = 19
n = len(nums)
low = 0
high = n-1
pos = -1
while low <= high:
    mid = (high+low)//2
    if nums[mid] == target:
        pos = mid
        break
    if nums[mid] <= nums[high]:
        if nums[mid] <= target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1
    else:
        if nums[low] <= target <= nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
print(pos) # O(log(N))