def solution(rows, columns, queries):
    arr = [[num for num in range(row*columns+1,row*columns+1+columns)] for row in range(rows)]

    answer = []
    for query in queries:
    # query = queries[0]

        query = [q-1 for q in query]
        up = query[0]
        left = query[1]
        down = query[2]
        right = query[3]

        boundary = arr[up][left:right] + [arr[row][right] for row in range(up,down)] + arr[down][right:left:-1] + [arr[row][left] for row in range(down,up,-1)]
        answer.append(min(boundary))
        last = boundary.pop()
        boundary = [last] + boundary

        ind = 0
        # [up,left]
        for col in range(left,right):
            arr[up][col] = boundary[ind]
            ind += 1

        for row in range(up,down):
            arr[row][right] = boundary[ind]
            ind += 1

        for col in range(right,left,-1):
            arr[down][col] = boundary[ind]
            ind += 1

        for row in range(down, up, -1):
            arr[row][left] = boundary[ind]
            ind += 1



    # 순서 : [up,left] -> [up,right] -> [down, right] -> [down, left]

    return answer

