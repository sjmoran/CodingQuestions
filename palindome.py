def lps(str):

    n = len(str)
    L = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        L[i][i] = 1

    for i in range(n - 1):
        if str[i] == str[i + 1]:
            L[i][i + 1] = 2
        else:
            L[i][i + 1] = 1

    for l in range(3, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if str[j] == str[i]:
                L[i][j] = 2 + L[i + 1][j - 1]

            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j])

    return L[0][n - 1]


seq = "seannaes"
opt = lps(seq)
print opt
