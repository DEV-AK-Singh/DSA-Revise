mat = [[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]

def print_mat(mat):    
    r = len(mat)
    c = len(mat[0])
    for i in range(0,r):
        for j in range(0,c):
            print(mat[i][j], end=" ")
        print("")

r = len(mat)
c = len(mat[0])

row_track = [0 for _ in range(r)]
col_track = [0 for _ in range(c)]

print_mat(mat)

for i in range(0,r):
    for j in range(0,c):
        if mat[i][j] == 0:
            row_track[i] = -1
            col_track[j] = -1

for i in range(0,r):
    for j in range(0,c):
        if row_track[i] == -1 or col_track[j] == -1:
            mat[i][j] = 0

print()

print_mat(mat)