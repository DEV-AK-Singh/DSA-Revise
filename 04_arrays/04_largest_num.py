nums = [55,32,-97,99,3,67]
largest = nums[0]
smallest = nums[0]
for i in range(0, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
    if nums[i] < smallest:
        smallest = nums[i]
print(smallest, largest)