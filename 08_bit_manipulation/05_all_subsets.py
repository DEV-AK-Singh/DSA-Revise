nums = [1,2,3]
l = len(nums)
n = 1 << len(nums)
res = []
for i in range(0, n):
    temp = []
    for index in range(0, l):
        if i & (1 << index):
            temp.append(nums[index])
    res.append(temp)
print(res) # O(2^n) X O(n) 