'''
Title : 나무 재테크
Link : https://www.acmicpc.net/problem/16235
'''
import sys, collections

input = sys.stdin.readline

class tree_farm:
    def __init__(self, n, A, t):
        self.size = n
        self.farm = [[5] * n for _ in range(n)]
        self.tree = t
        self.nutrient = A

    def spring(self):
        '''
        봄과정 진행, 진행못하는 칸에 대하여 여름과정까지 동시 진행
        '''
        new_tree = [[collections.defaultdict(int) for _ in range(self.size)] for _ in range(self.size)]
        dead_tree = [[0] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if len(self.tree[i][j]) == 0:
                    continue
                # 각 나무의 봄 & 여름 과정 진행
                # 나무 크기별로 봄 & 여름과정 진행 가능한지 확인
                for k in sorted(self.tree[i][j].keys()):
                    if k * self.tree[i][j][k] <= self.farm[i][j]:
                        self.farm[i][j] -= k * self.tree[i][j][k]
                        new_tree[k + 1] = self.tree[i][j][k]
                    elif k <= self.farm[i][j] < k * self.tree[i][j][k]:
                        k2 = self.farm[i][j] // k
                        self.farm[i][j] -= k2 * self.tree[i][j][k]
                        new_tree[k + 1] = k2
                        dead_tree[i][j] += (k // 2) * (self.tree[i][j][k] - k2)
                    else:
                        dead_tree[i][j] += (k // 2) (self.tree[i][j][k])
        self.summer(dead_tree)
        self.tree = new_tree

    def summer(self, dead_tree: list):
        for i in range(self.size):
            for j in range(self.size):
                self.farm[i][j] += dead_tree[i][j]

    def new_tree(self, i: int, j: int, count: int):
        '''
        가을 과정에서 5의 배수인 나무 count만큼 인접 칸에 나무 생성
        '''     
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        for t in range(8):
            x, y = i + dx[t], j + dy[t]
            if x < 0 or x >= self.size:
                continue
            if y < 0 or y >= self.size:
                continue
            for _ in range(count):
                self.tree[x][y].appendleft(1)

    def autumn(self):
        '''
        모든 칸에 대하여 가을 과정 진행하기 위해 5의 배수인 나무 개수 확인
        '''
        for i in range(self.size):
            for j in range(self.size):
                count = 0
                for k in sorted(self.tree[i][j].keys()):
                    if k % 5 == 0:
                        count += self.tree[i][j][k]
                self.new_tree(i, j, count)
        
        for i in range(self.size):
            for j in range(self.size):
                count = 0
                if self.tree[i][j] == []:
                    continue
                for t in self.tree[i][j]:
                    if t % 5 == 0:
                        count += 1
                if count == 0:
                    continue
                self.new_tree(i, j, count)

    def winter(self):
        '''
        겨울과정, 모든칸에 추가 영양분 투입
        '''
        for i in range(self.size):
            for j in range(self.size):
                self.farm[i][j] += self.nutrient[i][j]

    def year(self, years: int):
        '''
        입력 년수 years에 따라 봄, 여름, 가을, 겨울 과정 진행
        '''
        for _ in range(years):
            self.spring()
            self.autumn()
            self.winter()

    def count_tree(self) -> int:
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                count += len(self.tree[i][j])
        return count


# 농장 크기, 심은 나무, 확인할 년수
n, m, k = map(int, input().split())
# 나무 농장, 추가할 영양분
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
# 심겨진 나무
tree = [[collections.defaultdict(int) for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1][z] + 1

# 상도의 나무 농장 초기화
sangdo = tree_farm(n, A, tree)
# 상도의 나무 농장 k년 반복
sangdo.year(k)
# 상도의 나무 농장 나무 개수 출력
print(sangdo.count_tree())
