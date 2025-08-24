nums = [5, 8, 1, 6, 9, 2, 4]

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

# j = 0

# for i in range(len(nums)-1, -1, -1):
#     for j in range(0, i):
#         if nums[j] > nums[j+1]:
#             swap(nums, j, j+1)

def bubble_sort_by_rec(nums, i, j):
    if i==0:
        return
    for j in range(0, i):
        if nums[j] > nums[j+1]:
            swap(nums, j, j+1)
    bubble_sort_by_rec(nums, i-1, j+1)

bubble_sort_by_rec(nums, len(nums)-1, 0)

print(nums)        
