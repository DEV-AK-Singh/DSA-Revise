arr = [-1,0,1,2,-1,-4] 
n = len(arr)

# {(-1, 0, 1), (-1, -1, 2)} -> solution

# # brute O(n3)
# res = set()
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             if arr[i] + arr[j] + arr[k] == 0:
#                 temp = (arr[i],arr[j],arr[k])
#                 res.add(tuple(sorted(temp)))
# print(res)

# # better O(n2) -> S(n)
# res = set() 
# for i in range(n):
#     temp = set()
#     for j in range(i+1, n):
#         third_key = -(arr[i]+arr[j])
#         if third_key in temp:
#             triplet = [arr[i], arr[j], third_key]
#             triplet.sort()
#             res.add(tuple(triplet))
#         temp.add(arr[j])
# print(res)

# optimal
