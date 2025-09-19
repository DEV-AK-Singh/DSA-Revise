nums = [1,2,3,4,3]

def nextGreaterElements(nums):
    n = len(nums)
    nums = nums * 2
    ans = [-1] * n
    stack = [] 
    for i in range(2*n - 1, -1, -1):
        while len(stack) != 0 and stack[-1] <= nums[i]:
            stack.pop()
        if len(stack) != 0 and i < n:
            ans[i] = stack[-1]
        stack.append(nums[i])
    return ans

print(nextGreaterElements(nums))