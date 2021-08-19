"""
Title : 이진 검색 트리
Link :  https://www.acmicpc.net/problem/5639
"""

import sys, collections
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


def postorder(child, now):
    if child[now][0]:
        postorder(child, child[now][0])
    if child[now][1]:
        postorder(child, child[now][1])
    print(now)


root = int(input())

parent = collections.defaultdict(int)
child = collections.defaultdict(lambda: [0, 0])

# 가장 최근 부모
p = root
# 점을 받으며 전위순회에 따라 저장
while True:
    try:
        n = int(input())
    except:
        break
    # n이 더 작은 경우 p의 왼쪽 노드로 들어가서 탐색
    if n < p:
        child[p][0] = n
        parent[n] = p
        p = n
    # p보다 더 큰 경우
    else:
        # 오른쪽 노드로 삼을 점 선택
        while True:
            # 조부모 노드가 없는 경우 == 부모가 루트인 경우
            # 부모노드의 오른쪽 자식으로
            if p == root:
                break
            # 조부모 노드보다 작은 경우
            # 부모노드의 오른쪽 자식으로
            elif n > p and n < parent[p]:
                break
            # 아니라면 조부모 노드로 가서 다시 탐색
            else:
                p = parent[p]
        # 오른쪽 자식을 확인하며 더 내려갈 수 있는지 확인
        while True:
            if child[p][1] and n > child[p][1]:
                p = child[p][1]
            else:
                break
        child[p][1] = n
        parent[n] = p
        p = n

# 전위 순회결과로 트리 생성 완료
# 후위 순회하며 결과 출력
postorder(child, root)



'''
Counter Example
1
2
3
asn : 3 2 1
output : 3 1
'''