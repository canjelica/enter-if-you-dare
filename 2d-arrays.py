def hourglassSum(arr):

    def calc_hrglass(x,y):
        top = arr[x][y] + arr[x][y+1] + arr[x][y+2]
        middle = arr[x+1][y+1]
        bottom = arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]

        return top + middle + bottom

    highest = calc_hrglass(0,0)

    for i in range(0,4):
        for j in range(0,4):
            highest = max(highest, calc_hrglass(i,j))
    
    return highest


    #approach, how to access variables; a certain number is the sum of everything around it
