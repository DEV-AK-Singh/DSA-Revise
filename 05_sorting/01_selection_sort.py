nums = [2,1,5,6,3,4,7]

# def selection_sort(nums):
#     length = len(nums)
#     for i in range(0, length):
#         min_idx = i
#         j = i+1
#         for j in range(j, length):
#             if j == length:
#                 break
#             if nums[j] < nums[min_idx]:
#                 min_idx = j
#         nums[i], nums[min_idx] = nums[min_idx], nums[i]

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

def find_min_idx(nums, start, end):
    min_idx = start
    curr = start
    while curr < end:
        if nums[curr] < nums[min_idx]:
            min_idx = curr 
        curr += 1
    return min_idx

def selection_sort_by_recursion(nums, start, end):
    if start == end:
        return
    min_idx = find_min_idx(nums, start, end) 
    swap(nums, start, min_idx)
    selection_sort_by_recursion(nums, start+1, end)

# selection_sort(nums)
selection_sort_by_recursion(nums, 0, len(nums))
print(nums)

