"""
Title : 중앙값 구하기
Link : https://www.acmicpc.net/problem/2696
"""

from heapq import heappush, heappushpop
from sys import stdin

input = stdin.readline
II = lambda: int(input())


if __name__ == "__main__":
    ans = ""
    for _ in range(II()):
        M = II()
        k = M // 10 if not M % 10 else M // 10 + 1
        seq = []
        for _ in range(k):
            seq.extend(list(map(int, input().split())))

        min_heap, max_heap = [], []
        tmp = []
        for i, x in enumerate(seq):
            if not i:
                max_heap.append(-x)
            elif len(max_heap) == len(min_heap):
                if x > -max_heap[0]:
                    heappush(max_heap, -heappushpop(min_heap, x))
                else:
                    heappush(max_heap, -x)
            else:
                if x > -max_heap[0]:
                    heappush(min_heap, x)
                else:
                    heappush(max_heap, -heappushpop(min_heap, x))
            if not i % 2:
                tmp.append(-max_heap[0])

        k = len(tmp) // 10 if not len(tmp) % 10 else len(tmp) // 10 + 1
        ans += f"{len(tmp)}\n"
        for i in range(k):
            if i == k - 1:
                ans += " ".join(tmp[i * 10 :]) + "\n"
            else:
                ans += " ".join(tmp[i * 10 : (i + 1) * 10 + 1]) + "\n"
    print(ans)
