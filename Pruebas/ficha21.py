# p = []
# for i in range(3):
#     p.append([])
#     for j in range(2):
#         p[i].append([])
#         for k in range(4):
#             p[i][j].append([])
#
# p[2][1][3] = 'Prueba'
# print(p)

def test(mat):
    n = len(mat)
    m = len(mat[0])
    r = [n*[0] for k in range(m)]

    for i in range(n):
        for j in range(m):
            r[j][i] = mat[i][j]

    return r


if __name__ == '__main__':
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    test(matriz)
