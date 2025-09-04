nums = [1, 2, 1]
n = len(nums)
results = [] 

def subsets(index, total):
    if index >= n:
        results.append(total)
        return 
    subsets(index+1, total+nums[index])
    subsets(index+1, total)

subsets(0, 0)

results.sort()

print(results)

    
