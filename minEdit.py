import numpy as np

def minEditDistance(source, target):
    m = len(source)
    n = len(target)
    def check(source,target):
        if source is target:
            return 0
        else:
            return 2
    matrix = [0 for i in range(n+1)]
    for i in range(n+1):
        matrix[i] = [0 for i in range(m+1)]
    for i in range(1,n+1):
        matrix[i][0] = matrix[i-1][0] + 1
    for i in range(1, m+1):
        matrix[0][i] = matrix[0][i-1] + 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            matrix[i][j] = min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1] + check(source[j-1],target[i-1]))
        print(matrix[i])
    return matrix[n][m]
    

if __name__ == "__main__":
    source = "intent"
    target = "execution"
    print(minEditDistance(source, target))