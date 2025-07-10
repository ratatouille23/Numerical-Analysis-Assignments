def luDecomposition(mat, n):

    lower = [[0 for i in range(n)]
             for j in range(n)]
    upper = [[0 for i in range(n)]
             for j in range(n)]

    for i in range(n):
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            upper[i][k] = mat[i][k] - sum

        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                lower[k][i] = int((mat[k][i] - sum) /
                                  upper[i][i])

    print("Lower Triangular\t\tUpper Triangular")

    for i in range(n):
        for j in range(n):
            print(lower[i][j], end="\t")
        print("", end="\t")

        for j in range(n):
            print(upper[i][j], end="\t")
        print("")


if __name__ == "__main__":
    mat = [[2, -1, -2],
        [-4, 6, 3],
        [-4, -2, 8]]

    luDecomposition(mat, 3)
