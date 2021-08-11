"""
Title : 습격자 초라기
Link : https://www.acmicpc.net/problem/1006
"""



# 틀렸습니다
import sys
input = sys.stdin.readline


def check(i, j, d):
    if d == 0:
        if dp[i][j - 1]:
            return False
        else:
            return True
    elif d == 1:
        if dp[(i + 1) % 2][j]:
            return False
        else:
            return True
    else:
        if dp[i][(j + 1) % n]:
            return False
        else:
            return True


def reverse_check(i, j):
    if direction[i][j][0] == 1:
        a = dp[i][j]
    pass



for _ in range(int(input())):
    n, w = map(int, input().split())
    sector = [list(map(int, input().split())) for _ in range(2)]
    
    if n == 1:
        if sector[0][0] + sector[1][0] <= w:
            print(1)
        else:
            print(2)
        continue
    
    # 각각 왼쪽, 위/아래, 오른쪽에 같이 침투 가능한지
    direction = [[[0] * 3 for _ in range(n)] for _ in range(2)]
    for i in range(2):
        for j in range(n):
            now = sector[i][j]
            if now + sector[i][j - 1] <= w:
                direction[i][j][0] = 1
            if now + sector[(i + 1) % 2][j] <= w:
                direction[i][j][1] = 1
            if now + sector[i][(j + 1) % n] <= w:
                direction[i][j][2] = 1
    
    # 왼쪽 위/아래 오른쪽 우선순위 탐색
    dp = [[0] * n for _ in range(2)]
    
    agent1 = 1
    for i in range(2):
        for j in range(n):
            # 이미 배치했으면 넘어가기
            if dp[i][j]:
                continue
            # 주변과 이웃해서 배치 불가능한 경우
            elif sum(direction[i][j]) == 0:
                dp[i][j] = agent1
                agent1 += 1
            # 주변 한 칸 이상에에 이웃해서 배치가능한 경우
            # 왼쪽, 위/아래, 오른쪽 우선순위로 배치
            else:
                for idx in range(3):
                    if not direction[i][j][idx]:
                        continue
                    # 해당 방향의 칸이 이미 특수부대가 차지했는지 확인
                    if check(i, j, idx):
                        dp[i][j] = agent1
                        if idx == 0:
                            dp[i][j - 1] = agent1
                        elif idx == 1:
                            dp[(i + 1) % 2][j] = agent1
                        else:
                            dp[i][(j + 1) % n] = agent1
                        # 특수부대를 배치했으면 for문 종료
                        agent1 += 1
                        break
                # 어떤 방향에도 특수부대를 배치할 수 없을 때
                else:
                    dp[i][j] = agent1
                    agent1 += 1
    
    # 오른쪽 위/아래 왼쪽 우선순위 탐색
    dp = [[0] * n for _ in range(2)]
    
    agent2 = 1
    for i in range(2):
        for j in range(n):
            # 이미 배치했으면 넘어가기
            if dp[i][j]:
                continue
            # 주변과 이웃해서 배치 불가능한 경우
            elif sum(direction[i][j]) == 0:
                dp[i][j] = agent2
                agent2 += 1
            # 주변 한 칸 이상에에 이웃해서 배치가능한 경우
            # 왼쪽, 위/아래, 오른쪽 우선순위로 배치
            else:
                for idx in range(2, -1, -1):
                    if not direction[i][j][idx]:
                        continue
                    # 해당 방향의 칸이 이미 특수부대가 차지했는지 확인
                    if check(i, j, idx):
                        dp[i][j] = agent2
                        if idx == 0:
                            dp[i][j - 1] = agent2
                        elif idx == 1:
                            dp[(i + 1) % 2][j] = agent2
                        else:
                            dp[i][(j + 1) % n] = agent2
                        # 특수부대를 배치했으면 for문 종료
                        agent2 += 1
                        break
                # 어떤 방향에도 특수부대를 배치할 수 없을 때
                else:
                    dp[i][j] = agent2
                    agent2 += 1
    
    # 위/아래 왼쪽 오른쪽 우선순위 탐색
    dp = [[0] * n for _ in range(2)]
    
    agent3 = 1
    for i in range(2):
        for j in range(n):
            # 이미 배치했으면 넘어가기
            if dp[i][j]:
                continue
            # 주변과 이웃해서 배치 불가능한 경우
            elif sum(direction[i][j]) == 0:
                dp[i][j] = agent3
                agent3 += 1
            # 주변 한 칸 이상에에 이웃해서 배치가능한 경우
            # 왼쪽, 위/아래, 오른쪽 우선순위로 배치
            else:
                for idx in [1, 0, 2]:
                    if not direction[i][j][idx]:
                        continue
                    # 해당 방향의 칸이 이미 특수부대가 차지했는지 확인
                    if check(i, j, idx):
                        dp[i][j] = agent3
                        if idx == 0:
                            dp[i][j - 1] = agent3
                        elif idx == 1:
                            dp[(i + 1) % 2][j] = agent3
                        else:
                            dp[i][(j + 1) % n] = agent3
                        # 특수부대를 배치했으면 for문 종료
                        agent3 += 1
                        break
                # 어떤 방향에도 특수부대를 배치할 수 없을 때
                else:
                    dp[i][j] = agent3
                    agent3 += 1
    
    # 위/아래 오른쪽 왼쪽 우선순위 탐색
    dp = [[0] * n for _ in range(2)]
    
    agent4 = 1
    for i in range(2):
        for j in range(n):
            # 이미 배치했으면 넘어가기
            if dp[i][j]:
                continue
            # 주변과 이웃해서 배치 불가능한 경우
            elif sum(direction[i][j]) == 0:
                dp[i][j] = agent4
                agent4 += 1
            # 주변 한 칸 이상에에 이웃해서 배치가능한 경우
            # 왼쪽, 위/아래, 오른쪽 우선순위로 배치
            else:
                for idx in [1, 2, 0]:
                    if not direction[i][j][idx]:
                        continue
                    # 해당 방향의 칸이 이미 특수부대가 차지했는지 확인
                    if check(i, j, idx):
                        dp[i][j] = agent4
                        if idx == 0:
                            dp[i][j - 1] = agent4
                        elif idx == 1:
                            dp[(i + 1) % 2][j] = agent4
                        else:
                            dp[i][(j + 1) % n] = agent4
                        # 특수부대를 배치했으면 for문 종료
                        agent4 += 1
                        break
                # 어떤 방향에도 특수부대를 배치할 수 없을 때
                else:
                    dp[i][j] = agent4
                    agent4 += 1
    
    # 왼쪽 오른쪽 위/아래 우선순위 탐색
    dp = [[0] * n for _ in range(2)]
    
    agent5 = 1
    for i in range(2):
        for j in range(n):
            # 이미 배치했으면 넘어가기
            if dp[i][j]:
                continue
            # 주변과 이웃해서 배치 불가능한 경우
            elif sum(direction[i][j]) == 0:
                dp[i][j] = agent5
                agent5 += 1
            # 주변 한 칸 이상에에 이웃해서 배치가능한 경우
            # 왼쪽, 위/아래, 오른쪽 우선순위로 배치
            else:
                for idx in [0, 2, 1]:
                    if not direction[i][j][idx]:
                        continue
                    # 해당 방향의 칸이 이미 특수부대가 차지했는지 확인
                    if check(i, j, idx):
                        dp[i][j] = agent5
                        if idx == 0:
                            dp[i][j - 1] = agent5
                        elif idx == 1:
                            dp[(i + 1) % 2][j] = agent5
                        else:
                            dp[i][(j + 1) % n] = agent5
                        # 특수부대를 배치했으면 for문 종료
                        agent5 += 1
                        break
                # 어떤 방향에도 특수부대를 배치할 수 없을 때
                else:
                    dp[i][j] = agent5
                    agent5 += 1
    
    # 오른쪽 왼쪽 위/아래 우선순위 탐색
    dp = [[0] * n for _ in range(2)]
    
    agent6 = 1
    for i in range(2):
        for j in range(n):
            # 이미 배치했으면 넘어가기
            if dp[i][j]:
                continue
            # 주변과 이웃해서 배치 불가능한 경우
            elif sum(direction[i][j]) == 0:
                dp[i][j] = agent6
                agent6 += 1
            # 주변 한 칸 이상에에 이웃해서 배치가능한 경우
            # 왼쪽, 위/아래, 오른쪽 우선순위로 배치
            else:
                for idx in [2, 0, 1]:
                    if not direction[i][j][idx]:
                        continue
                    # 해당 방향의 칸이 이미 특수부대가 차지했는지 확인
                    if check(i, j, idx):
                        dp[i][j] = agent6
                        if idx == 0:
                            dp[i][j - 1] = agent6
                        elif idx == 1:
                            dp[(i + 1) % 2][j] = agent6
                        else:
                            dp[i][(j + 1) % n] = agent6
                        # 특수부대를 배치했으면 for문 종료
                        agent6 += 1
                        break
                # 어떤 방향에도 특수부대를 배치할 수 없을 때
                else:
                    dp[i][j] = agent6
                    agent6 += 1
    
    
    print(min(agent1, agent2, agent3, agent4, agent5, agent6) - 1)