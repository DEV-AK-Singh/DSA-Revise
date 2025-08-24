arr = [5, 7, 3, 2, 6, 1, 5, 9]
left = 0
right = 7

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

def rev(left, right, arr):
    if left >= right:
        return
    swap(left, right, arr)
    rev(left+1, right-1, arr)

rev(left=left, right=right, arr=arr)

print(arr)