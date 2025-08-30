nums = [11,11,11,11,11,11,11,1,3,4,5,11,11]
target = 12
n = len(nums)
low = 0
high = n-1
pos = -1
while low <= high:
    mid = (high+low)//2
    if nums[mid] == target:
        pos = mid
        break
    if nums[mid] == nums[high] == nums[low]:
        low += 1
        high -= 1
        continue
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
print(True if pos != -1 else False) # O(log(N)), worst->O(N)