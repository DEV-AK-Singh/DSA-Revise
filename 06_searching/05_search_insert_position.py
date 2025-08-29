arr = [1,3,4,5,8,9,14,15,19,20,21]
target = [5,20,2,17]

# brute
for target_val in target:
    for i in range(len(arr)):
        if arr[i] == target_val:
            print(i)
            break
        if arr[i] > target_val:
            print(i)
            break

# # optimal
# for target_val in target:
#     n = len(arr)
#     low = 0
#     high = n-1
#     lb = n
#     up = n
#     while high>=low:
#         mid = (low+high)//2
#         if target_val <= arr[mid]:
#             lb = mid
#             high = mid - 1 
#         else:
#             low = mid + 1
#     print(lb)
