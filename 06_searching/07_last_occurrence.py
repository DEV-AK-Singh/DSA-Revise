nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
n = len(nums)

target = -12

# brute -> O(n)
# first = -1
# last = -1 
# for i in range(n):
#     if target == nums[i]:
#         if first == -1:
#             first = i
#         last = i
# print([first,last])

# optimal -> O(2log(n)) -> O(log(n))
lb = -1 
low = 0
high = n-1
while high >= low:
    mid = (high+low)//2
    if nums[mid] >= target:
        high = mid - 1
        lb = mid
    else:
        low = mid + 1

ub = -1 
low = 0
high = n-1
while high >= low:
    mid = (high+low)//2
    if nums[mid] > target:
        high = mid - 1
        ub = mid
    else:
        low = mid + 1 

# print([lb,ub]) both lb and ub are equal incase if the both not present

if ub == lb:
    print([-1,-1])
else:
    print([lb,ub-1])