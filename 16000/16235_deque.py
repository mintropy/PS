'''
Title : 나무 재테크
Link : https://www.acmicpc.net/problem/16235
'''
import sys, collections

input = sys.stdin.readline

class tree_farm:
    def __init__(self, n, f, t):
        self.size = n
        self.farm = [[5] * n for _ in range(n)]
        self.tree = t
        self.nutrient = f

    def spring(self):
        '''
        봄과정 진행, 진행못하는 칸에 대하여 여름과정까지 동시 진행
        '''
        for i in range(self.size):
            for j in range(self.size):
                if len(self.tree[i][j]) == 0:
                    continue
                # 각 나무의 봄 & 여름 과정 진행
                # 나무에게 영양분을 줄 수 있으면 봄 과정 진행
                # 불가능하면, 그 다음 나무부터 여름과정 진행
                for k in range(len(self.tree[i][j])):
                    t = self.tree[i][j][k]
                    if t <= self.farm[i][j]:
                        self.farm[i][j] -= t
                        self.tree[i][j][k] += 1
                    else:
                        # 진행 못하는 나무들은 여름과정 진행
                        self.summer(i, j, len(self.tree[i][j]) - k)
                        break

    def summer(self, i: int, j: int, k: int):
        for _ in range(k):
            self.farm[i][j] += self.tree[i][j].pop() // 2

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
# 나무 농장
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
# 심겨진 나무
tree_tmp = [[[] for _ in range(n)] for _ in range(n)]
tree = [[collections.deque([]) for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree_tmp[x - 1][y - 1].append(z)
# 각 칸마다 나무의 나이순으로 정렬
for i in range(n):
    for j in range(n):
        tree[i][j].extend(sorted(tree_tmp[i][j]))

# 상도의 나무 농장 초기화
sangdo = tree_farm(n, A, tree)
# 상도의 나무 농장 k년 반복
sangdo.year(k)
# 상도의 나무 농장 나무 개수 출력
print(sangdo.count_tree())
