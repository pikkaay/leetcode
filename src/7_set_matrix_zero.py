'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    idict = set()
    jdict = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                idict.add(i)
                jdict.add(j)
    print(idict)
    print(jdict)

    for i in idict:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0
    for i in jdict:    
        for j in range(len(matrix)):
            matrix[j][i] = 0


matrix = [
[1,1,1],
[0,1,1],
[1,1,1]]
setZeroes(matrix)
print(matrix)

'''
[
[0, 1, 1], 
[0, 0, 0], 
[0, 1, 1]]


[
[1, 1, 1], 
[0, 0, 0], 
[1, 1, 1]]
'''
