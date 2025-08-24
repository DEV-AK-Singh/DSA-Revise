nums = [4,1,7,6,3,2,8]

def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high
    while i<j:
        while nums[i] <= pivot and i<=high-1:
            i += 1
        while nums[j] > pivot and j>=low+1:
            j -= 1
        if i<j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[j], nums[low] = nums[low], nums[j]   
    return j

def quick_sort(nums, low, high):
    if low < high:
        p_idx = partition(nums, low, high)
        quick_sort(nums, low, p_idx-1)
        quick_sort(nums, p_idx+1, high)

quick_sort(nums, 0, len(nums)-1)

print(nums)