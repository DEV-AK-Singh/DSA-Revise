# mat = [[1,2,3],[4,5,6],[7,8,9]]

# rows = len(mat)
# cols = len(mat[0])

# # print upper-triangle
# for i in range(0,rows):
#     for j in range(0,cols):
#         if j>i:
#             print(mat[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print("")

# print("\n")

# # print lower-triangle
# for i in range(0,rows):
#     for j in range(0,cols):
#         if j<i:
#             print(mat[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print("")

# print("\n")

# # print diagonal
# for i in range(0,rows):
#     for j in range(0,cols):
#         if j==i:
#             print(mat[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print("")

# print("\n")

# # print cross-diagonal
# for i in range(0,rows):
#     for j in range(0,cols):
#         if j+i==2:
#             print(mat[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print("")

mat = [[5,9,1],[2,3,7]]
# transpose
trans = []
for i in range(0,len(mat[0])):
    temp = []
    for j in range(0,len(mat)):
        temp.append(mat[j][i])
    trans.append(temp)
print(trans)
