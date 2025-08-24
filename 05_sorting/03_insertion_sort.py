nums = [3,5,6,4,8,9,10,7,1]

# for i in range(1, len(nums)):
#     if nums[i-1] <= nums[i]:
#         pass
#     else:
#         key = nums[i]
#         j = i-1
#         while j>=0 and nums[j] > key:
#             nums[j+1] = nums[j]
#             j -= 1
#         nums[j+1] = key
        
# print(nums)

length = len(nums)

def insertion_sort_by_rec(nums, i, length): 
    if i>=length:
        return
    if nums[i-1] <= nums[i]:
        pass
    else:
        key = nums[i] 
        j = i-1
        while j>=0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key 
    insertion_sort_by_rec(nums, i+1, length)

insertion_sort_by_rec(nums, 1, length)

print(nums)