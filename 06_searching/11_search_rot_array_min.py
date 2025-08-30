nums = [2,3,4,5,6,7,8,9,1]
n = len(nums)
low = 0
high = n - 1
min_val = float("inf")
while low <= high:
    mid = (high+low)//2 
    if nums[mid] <= nums[high]:
        min_val = min(min_val, nums[mid])
        high = mid - 1
    else:
        min_val = min(min_val, nums[low])
        low = mid + 1
print(min_val) # O(log(N))