arr = [1,1,1,1,2,2,3,3,4,4,5,5,5,5]
n = len(arr)
target = 8
# better O(n3)->S(n)
res = set()
for i in range(n):
    for j in range(i+1,n):
        temp = set()
        for k in range(j+1,n):
            forth_key = target-(arr[i]+arr[j]+arr[k])
            if forth_key in temp:
                res.add(tuple(sorted([arr[i],arr[j],arr[k],forth_key])))
            else:
                temp.add(arr[k])
print(res)

# optimal O(n3)->S(1)
res = set()
arr.sort()
for i in range(n):
    if i != 0 and arr[i] == arr[i-1]:
        continue
    for j in range(i+1,n):
        if j > i+1 and arr[j] == arr[j-1]:
            continue
        k = j+1
        l = n-1
        while k<l:
            sum = arr[i]+arr[j]+arr[k]+arr[l]
            if sum == target:
                res.add(tuple([arr[i],arr[j],arr[k],arr[l]]))           
                k+=1
                l-=1
                # while k<l and arr[k]==arr[k+1]:
                #     k+=1
                # while k<l and arr[l]==arr[l-1]:
                #     l-=1
            elif sum < target:
                k+=1
            else:
                l-=1
print(res)