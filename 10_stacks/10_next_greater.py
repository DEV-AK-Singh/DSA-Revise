arr = [6, 8, 0, 1, 3]

def next_greater(arr):
    n = len(arr)
    stack = []
    ans = [-1] * n
    for i in range(n-1, -1, -1):
        while len(stack) != 0 and stack[-1] <= arr[i]:
            stack.pop()
        if len(stack) != 0:
            ans[i] = stack[-1]
        stack.append(arr[i])
    return ans

print(next_greater(arr))