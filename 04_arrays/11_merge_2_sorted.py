nums1 = [1,1,1,2,4,6,7]
nums2 = [1,2,3,6,7,8,9,10]

result = []

n = len(nums1)
m = len(nums2)
i,j = 0,0

while i<n and j<m:
    if len(result) != 0:
        if result[-1]==nums1[i]:
            while result[-1]==nums1[i] and i<n:
                i+=1
        if result[-1]==nums2[j]:
            while result[-1]==nums2[j] and j<m:
                j+=1
    if nums1[i]==nums2[j]:
        result.append(nums1[i])
    elif nums1[i]>nums2[j]:
        result.append(nums2[j])
        result.append(nums1[i])
    else:
        result.append(nums1[i])
        result.append(nums2[j])
    i+=1
    j+=1

if i<n:
    while i<n:
        if result[-1] != nums1[i]:
            result.append(nums1[i])
        i+=1

if j<m:
    while j<m:
        if result[-1] != nums2[j]:
            result.append(nums2[j])
        j+=1

print(result)