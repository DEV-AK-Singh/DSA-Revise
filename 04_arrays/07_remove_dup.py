arr = [1,1,2,3,3,3,4,4,5,5,6]

n=len(arr)
i=0
j=i+1
while j<n:
    if arr[j] != arr[i]:
        arr[i+1], arr[j] = arr[j], arr[i+1]
        i+=1
    j+=1
print(arr)
print("Unique:",i+1)
