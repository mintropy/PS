from sys import stdin


def floyd_warshall():
    '''
    n = int(stdin.readline())
    edges = []
    for _ in range(n):
        edges.append(list(map(int, stdin.readline().split())))
    '''

    n = 3
    edges = [[0,1,0],[0,0,1],[1,0,0]]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if edges[i][k] + edges[k][j] == 2:
                    edges[i][j] = 1

    for i in range(n):
        for j in range(n):
            print(edges[i][j], end = ' ')
        print()


floyd_warshall()