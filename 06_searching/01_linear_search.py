nums = [4,1,7,6,3,2,8]

def linear_search(nums, target):
    for i in range(0,len(nums)):
        if target==nums[i]:
            return i
    return -1

print(linear_search(nums,9))