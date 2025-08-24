nums = [1,2,3,4,5,6]

def n_right_rotation(nums, n):
    return nums[n:]+nums[:n]

def n_left_rotation(nums, n):
    return nums[-n:]+nums[:-n]

print(n_right_rotation(nums,1))
print(n_right_rotation(nums,2))
print(n_left_rotation(nums,1))
print(n_left_rotation(nums,2))