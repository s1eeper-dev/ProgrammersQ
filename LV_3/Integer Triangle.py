#https://programmers.co.kr/learn/courses/30/lessons/43105

#input
triangle = [[7],
            [3, 8],
            [8, 1, 0],
            [2, 7, 4, 4],
            [4, 5, 2, 6, 5]]
#result: 30

#solution

for i in range(1,len(triangle)):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == len(triangle[i])-1:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
        
answer = max(triangle[len(triangle)-1])

    
#오답 없
