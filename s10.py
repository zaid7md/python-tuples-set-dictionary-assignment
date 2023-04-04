#WAP to store a sparse matrix as a dictionary. 

sparse_matrix = [[0, 0, 0, 1, 0],
       [6, 0, 5, 0, 3],
       [10, 0, 2, 4, 0]]
 

dic = {}
 
for i in range(len(sparse_matrix)):
    for j in range(len(sparse_matrix[i])):
        if sparse_matrix[i][j] != 0:
            dic[i, j] = sparse_matrix[i][j]

print(dic)