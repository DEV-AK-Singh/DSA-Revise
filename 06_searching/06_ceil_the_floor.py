nums = [3,4,4,4,8,9,9,10,12,12,14,15]
n = len(nums)
target = [8,11,2,20]
for t in target:
    low = 0
    high = n-1
    floor = -1 
    ceil = -1 
    while low <= high:
        mid = (high+low)//2
        if nums[mid] == t:
            floor, ceil = nums[mid], nums[mid] 
            break
        elif nums[mid] > t:
            ceil = nums[mid]
            high = mid-1
        else:
            floor = nums[mid]
            low = mid+1
    print([floor,ceil])
