k = 3
sum = 9   
nums = [1,2,3,4,5,6,7,8,9]  
result = []
n = len(nums)
def backtrack(index, total, subset):
    if index >= n:
        if total == sum and len(subset) == k:
            result.append(subset.copy())
        return
    if total > sum:
        return 
    subset.append(nums[index])
    backtrack(index+1, total+nums[index], subset)
    subset.pop()
    backtrack(index+1, total, subset)

backtrack(0, 0, [])

print(result)
