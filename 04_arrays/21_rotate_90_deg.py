def print_matrix(mat):
    n = len(mat)
    m = len(mat)
    for i in range(0, n):
        for j in range(0, m):
            print(mat[i][j], end=" ")
        print()
    print()

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
## brute
# result = [[0 for _ in range(len(mat))] for _ in range(len(mat[0]))]

# for i in range(0,len(mat)):
#     for j in range(0,len(mat[0])):
#         result[j][len(mat)-1-i] = mat[i][j]

# for i in range(0,len(mat)):
#     for j in range(0,len(mat[0])):
#         print(result[i][j], end=" ")
#     print("")

# optimal
# transpose -> reverse
print_matrix(mat)

for i in range(0, len(mat)):
    for j in range(0, len(mat[0])):
        if i > j:
            mat[j][i] ,mat[i][j] = mat[i][j], mat[j][i]

for i in range(0, len(mat)):
    for j in range(0, int(len(mat[0])/2)):
        mat[i][j], mat[i][len(mat[0])-1-j] = mat[i][len(mat[0])-1-j], mat[i][j]

print_matrix(mat)