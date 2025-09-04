nums = [10,1,2,7,6,1,5]

target = 8
n = len(nums) 

# # brute
# results = set() 
# def backtracking(index, total, combination):
#     if total == target:
#         # results.add(tuple(sorted(combination).copy()))
#         results.add(tuple(combination.copy()))
#         return   
#     if total > target or index >= n:
#         return
#     combination.append(nums[index])
#     backtracking(index+1, total+nums[index], combination)    
#     combination.pop()
#     backtracking(index+1, total, combination)
# backtracking(0,0,[])
# print(list([list(ele) for ele in results]))

# optimal

results = []
total = target
nums.sort()
# solve using backtracking in optimal way

def backtrack(index, combination, total):
    if total == 0:
        results.append(combination.copy())
        return
    if total < 0 or index >= n:
        return
    for i in range(index, n):
        if i > index and nums[i] == nums[index]:
            continue 
        if nums[i] > total:
            break
        combination.append(nums[i])
        backtrack(i+1, combination, total-nums[i])
        combination.pop()

backtrack(0, [], total)
print(results)