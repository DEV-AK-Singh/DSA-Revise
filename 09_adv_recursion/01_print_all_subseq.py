nums = [1,2,3] 
result = []

def all_sub_seq(index, subset):
    if index >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[index])
    all_sub_seq(index+1, subset)
    subset.pop()
    all_sub_seq(index+1, subset)

all_sub_seq(0, [])

print(result)
