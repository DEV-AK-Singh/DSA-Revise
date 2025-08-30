nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
n = len(nums)

target = 3

# # brute 
# count = 0
# for ele in nums:
#     if ele == target:
#         count += 1
# print(count)

# optimal -> O(2log(n)) -> O(log(n))
lb = n 
low = 0
high = n-1
while high >= low:
    mid = (high+low)//2
    if nums[mid] >= target:
        high = mid - 1
        lb = mid
    else:
        low = mid + 1

ub = n
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
    print(0)
else:
    print(ub-lb)