nums = [2,3,6,7]
target = 7
n = len(nums) 
results = [] 

def backtracking(index, total, combination):
    if total == target:
        results.append(combination.copy())
        return   
    if total > target or index >= n:
        return
    combination.append(nums[index])
    backtracking(index, total+nums[index], combination)    
    combination.pop()
    backtracking(index+1, total, combination)

backtracking(0,0,[])

print(results)