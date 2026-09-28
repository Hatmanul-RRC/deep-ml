def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    n = len(a[0])
    m = len(b)
    if n != m:
        return -1

    c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            c[i][j] = 0
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    return c