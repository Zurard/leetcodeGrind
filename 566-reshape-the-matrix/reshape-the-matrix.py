class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        if r*c != len(mat) * len(mat[0]):
            return mat

        order = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                order.append(mat[i][j])


        mat = [[0]*c for _ in range(r)]
        print(mat)

        x,y = 0 , 0 
        for num in order:
            if y == c:
                y = 0  
                x+=1
            mat[x][y] = num        
            y+=1
        print(mat)
        return mat