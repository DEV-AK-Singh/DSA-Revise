nums = [5,4,6,7,8,9,12,10,11]
target = 19

# # brute -> o(n2)
# def two_sum(nums):
#     n = len(nums)
#     for i in range(0, n):
#         for j in range(i, n):
#             if nums[i]+nums[j]==target:
#                 return (i,j)
# print(two_sum(nums))

# optimal -> o(n),s(n)
idx_dict = {}
for i in range(0,len(nums)):
    remaining_value = target-nums[i]
    if remaining_value in idx_dict:
        print(idx_dict[remaining_value],i)
        break
    else:
        idx_dict[nums[i]]=i
