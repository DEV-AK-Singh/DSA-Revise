nums = [1,2,4,4,6,7,6,3,1,2,1]
freq = dict() 
# freq = {}

# for i in range(0, len(nums)):
#     key = nums[i] 
#     if key in freq:
#         freq[key] += 1
#     else:
#         freq[key] = 1

for i in range(0, len(nums)):
    freq[nums[i]] =  freq.get(nums[i], 0) + 1
print(freq)