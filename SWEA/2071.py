"""
Title : 평균값 구하기
"""

for tc in range(1, int(input()) + 1):
    seq = list(map(int, input().split()))
    avg = int(sum(seq) / len(seq) + 0.5)
    print(f'#{tc} {avg}')