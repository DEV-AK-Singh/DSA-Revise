nums = [3,5,6,4,8,9,10,7,1]

def merge(left_arr, right_arr):
    i,j = 0,0
    n,m = len(left_arr),len(right_arr)
    result = []  
    while i < n and j < m:
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        elif left_arr[i] > right_arr[j]:
            result.append(right_arr[j])
            j += 1
        else:
            result.append(left_arr[i])
            result.append(right_arr[j])
            i += 1
            j += 1
    if i < n:
        while i < n:
            result.append(left_arr[i])
            i += 1
    if j < m:
        while j < m:
            result.append(right_arr[j])
            j += 1
    return result    
    
def merge_sort(arr):
    mid = len(arr)//2
    if mid < 1:
        return arr 
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:]) 
    return merge(left_arr, right_arr)

print(merge_sort(nums))
 
    