#from sys import stdin

# 인풋 받기
'''
n, m = map(int, stdin.readline().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, stdin.readline().split())))
'''

# 테스트 케이스
'''
n, m = 5, 5
paper = [[1,2,3,4,5],[5,4,3,2,1],[2,3,4,5,6],[6,5,4,3,2],[1,2,1,2,1]]
'''

n, m = 4, 4
#paper = [[1,2,0,0],[0,3,4,0],[0,0,0,0],[0,0,0,0]]
paper = [[0,0,0,0],[0,0,0,0],[0,0,3,4],[0,0,1,2]]


# 테트로미노 분류 및 정의
# 1, 3은 회전 불필요, 2는 회전하여 확인 필요
tetromino1 = [[1,1,1,1]]
tetromino2 = [[[0,0,1],[1,1,1]],
             [[1,0,0],[1,1,1]],
             [[0,1,1],[1,1,0]],
             [[1,1,0],[0,1,1]],
             [[0,1,0],[1,1,1]]
             ]
tetromino3 = [[1,1],[1,1]]

# 각 테트로미노가 올라갈 때 수의 합
def check(block, paper):
    count = 0
    h, w = len(block), len(block[0])
    for i in range(n - h + 1):
        for j in range(m - w + 1):
            tmp = 0
            for a in range(h):
                for b in range(w):
                    if block[a][b] == 1:
                        tmp += paper[i + a][j + b]
            if tmp > count:
                count = tmp
    return count


# 시계 방향으로 회전
def rotate(block):
    tmp = []
    h, w = len(block), len(block[0])
    for i in range(w):
        a = []
        for j in range(h):
            a.append(block[h - 1 - j][i])
        tmp.append(a)
    return(tmp)


def solution():
    ans = 0
    tet = []
    # 총 7개 케이스에 대하여 확인
    # tetromino1
    tet = tetromino1
    for i in range(2):
        x = check(tet, paper)
        if x > ans:
            ans = x
        tet = rotate(tet)

    # tetromino3
    tet = tetromino3
    x = check(tet, paper)
    if x > ans:
        ans = x

    # tetromino2
    for tet in tetromino2:
        for i in range(4):
            x = check(tet, paper)
            if x > ans:
                ans = x
            tet = rotate(tet)
    
    print(ans)
    return

solution()