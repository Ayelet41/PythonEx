#flip matrix in-place along its horizontal axis.
def flip_horizontal_axis(matrix):
    for i in range(len(matrix)/2):
        matrix[i],matrix[len(matrix)-1-i]=matrix[len(matrix)-1-i], matrix[i]    
        
        
def flip_horizontal_axis2(matrix):
    for line in range(len(matrix)/2):
        matrix[len(matrix)-1-line],matrix[line]=matrix[line],matrix[len(matrix)-line-1]
        return matrix        
        
