"""
Title : 트리인가?
Link : https://www.acmicpc.net/problem/6416
"""

import sys, collections
input = sys.stdin.readline


def find_root(tree_in, max_point):
    global point
    root_prob = []
    for i in range(1, max_point + 1):
        if tree_in[i] == []:
            root_prob.append(i)
    cnt = 0
    root = -1
    for prob in root_prob:
        if prob in point:
            cnt += 1
            root = prob
    
    if cnt == 1:
        return root
    else:
        return -1


def check_tree(tree_out, max_point, root):
    visited = [False] * (max_point + 1)
    visited[root] = True
    queue = collections.deque([root])
    while queue:
        p = queue.popleft()
        for q in tree_out[p]:
            if visited[q]:
                return False
            else:
                visited[q] = True
                queue.append(q)
    return True


tc = 1

while True:
    point = []
    while True:
        tmp = list(map(int, input().split()))
        point += tmp
        if tmp[-1] == 0 and tmp[-2] == 0:
            break
    max_point = 0
    # 트리 구성
    tree_in = collections.defaultdict(list)
    tree_out = collections.defaultdict(list)
    for i in range(0, len(point) // 2 - 1):
        a, b = point[i * 2], point[i * 2 + 1]
        tree_in[b].append(a)
        tree_out[a].append(b)
        max_point = max(max_point, a, b)
    
    # 트리인지 확인
    # 1. 루트 찾기 : 들어오는 선분이 없는 점 찾기
    
    root = find_root(tree_in, max_point)
    
    if root == -1 or not check_tree(tree_out, max_point, root):
        print(f'Case {tc} is not a tree.')
    else:
        print(f'Case {tc} is a tree.')
    
    try:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
    except:
        tc += 1
        continue