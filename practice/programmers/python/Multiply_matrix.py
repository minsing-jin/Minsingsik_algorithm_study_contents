# my 미천한 solution
def solution(arr1, arr2):
    ans = [[0 for i in range(len(arr2[0]))] 
           for n in range(len(arr1))]
    #print(ans)
    arr1_row = [row for row in range(len(arr1))]
    arr1_col = [col for col in range(len(arr1[0]))]
    arr2_row = [row for row in range(len(arr2))]


    #print(arr1_row)
    #print(arr1_col)
    #print(arr2_row)
    #print(arr2_col)


    for row_1 in arr1_row:
        #print('row_1: ' + str(row_1))
        col_2 = 0
        while col_2 < len(ans[0]):
            for col_1,row_2 in zip(arr1_col,arr2_row):
                #print('col_1: ' + str(col_1))
                #print('row_2: ' + str(row_2))
                ans[row_1][col_2] += arr1[row_1][col_1]*arr2[row_2][col_2]
            col_2 += 1
    #print(ans)
    return ans
  
 


# other sol
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]



import numpy as np
def productMatrix(A, B):

    return (np.matrix(A)*np.matrix(B)).tolist()

