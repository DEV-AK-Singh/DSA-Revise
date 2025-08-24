nums = [9,6,4,2,3,5,7,0,1]
n = len(nums)

# # brute -> o(n2),s(n)
# actual = [i for i in range(0, n)]
# for ele in actual:
#     if nums.count(ele) > 0:
#         pass
#     else:
#         print(f"Number {ele} is not present")
        
# # better -> o(n),s(n)
# hash_map = [0]*(n)
# for i in range(0, n):
#     if nums[i] < n:
#         hash_map[nums[i]] = 1
# for i in range(0, n):
#     if hash_map[i] == 0:
#         print(f"Number {i} is not present")

# optimal -> o(n),s(1)
actual_sum = (n*(n+1))/2
current_sum = sum(nums)
print(f"Number {int(actual_sum-current_sum)} is not present")