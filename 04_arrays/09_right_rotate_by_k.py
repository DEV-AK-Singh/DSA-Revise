nums = [3,9,5,6,7,2,10,9]

# # brute
# n=len(nums)
# k=13
# rotations=k%n
# for _ in range(0,rotations):
#     e = nums.pop()
#     nums.insert(0,e)

# better
# slicing

# # optimal
# def reverse(nums,left,right):
#     while left<right:
#         nums[left],nums[right]=nums[right],nums[left]
#         left+=1
#         right-=1

# n=len(nums)
# k=5
# reverse(nums,0,n-k-1)
# reverse(nums,n-k,n-1)
# reverse(nums,0,n-1)

print(nums)