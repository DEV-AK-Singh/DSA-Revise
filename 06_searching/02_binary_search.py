arr = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
target = 20

# low = 0
# high = len(arr)-1
# while low < high:
#     mid = (high+low)//2
#     if arr[mid] < target:
#         print(f"mid {arr[mid]} smaller than target")
#         low = mid+1
#     elif arr[mid] > target:
#         print(f"mid {arr[mid]} larger than target")
#         high = mid-1
#     else:
#         print(f"Target found at index {mid}")
#         break

def bs(arr,low,high,target):
    mid = (high+low)//2
    if arr[mid] > target:
        print(f"mid {arr[mid]} larger than target")
        return bs(arr,low,mid-1,target)
    elif arr[mid] < target:
        print(f"mid {arr[mid]} smaller than target")
        return bs(arr,mid+1,high,target)
    else:
        return arr[mid]
    
print(bs(arr,0,len(arr)-1,target))
    
