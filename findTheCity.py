# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold):
        matrix = [[float("inf")] * n for i in range(n)]
        for i in range(n):
            matrix[i][i] = 0
        
        for edge in edges:
            matrix[edge[0]][edge[1]] = edge[2]
            matrix[edge[1]][edge[0]] = edge[2]

        print(matrix)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if matrix[k][i] == float("inf") or matrix[i][k] == float("inf"):
                        continue
                    matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])
        
        print(matrix)

        minNeighbour = float("inf")
        result = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if matrix[i][j] <= distanceThreshold:
                    count+=1
            if count <= minNeighbour:
                minNeighbour = count
                result = i
        return result
        



    

        
if __name__ == "__main__":
    Solution = Solution()
    edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
    print(Solution.findTheCity(5,edges,2))