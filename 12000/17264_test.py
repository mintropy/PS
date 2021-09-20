import sys
import heapq

input = sys.stdin.readline

n = int(input())
schedual = [tuple(map(int, input().split())) for _ in range(n)]
# 시작시간 오름차순 정렬
schedual.sort(key=lambda x:x[0])

# 지금 싸지방 사용하는 사람의 종료 시간
ssa_ji_bang = []
# 놀고있는 컴퓨터
sleeping_pc = []
# 각 컴퓨터를 몇 명이 하는지
pc_per_person = [0] * n

# 지금 최대로 사용한 pc 대수
pc_idx = 0

for st, end in schedual:
    # 싸지방 사용하는 사람 있을 때
    if ssa_ji_bang:
        # 더 빨리 종요하는 사람 있으면 모두 퇴장
        while ssa_ji_bang and ssa_ji_bang[0][0] <= st:
            _, idx = heapq.heappop(ssa_ji_bang)
            heapq.heappush(sleeping_pc, idx)
    # 다음 사람 싸지방에 넣기
    # 놀고 있는 컴퓨터 있으면 해당 컴퓨터로
    # 없으면 사람수에 해당하는 컴퓨터로
    if sleeping_pc:
        idx = heapq.heappop(sleeping_pc)
    else:
        idx = len(ssa_ji_bang)
    pc_per_person[idx] += 1
    heapq.heappush(ssa_ji_bang, (end, idx))
    # 사용 pc대수 확인
    if len(ssa_ji_bang) > pc_idx:
        pc_idx = len(ssa_ji_bang)

print(pc_idx)
print(*pc_per_person[:pc_idx])
