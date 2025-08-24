nums = [55,32,-97,99,3,67]

# #brute O(N)->NlogN
# nums.sort()
# print(nums[-2])

# # better O(N)->2N
# largest = float("-inf")
# second_largest = float("-inf")
# for i in range(0, len(nums)):
#     largest = max(largest, nums[i])
# for i in range(0, len(nums)):
#     second_largest = max(second_largest, nums[i]) if nums[i] < largest else second_largest
# print(second_largest, largest)

# optimal O(N)->N
largest = float("-inf")
second_largest = float("-inf")
for i in range(0, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
    if nums[i] > second_largest and nums[i] < largest:
        second_largest = nums[i]
print(second_largest, largest)
