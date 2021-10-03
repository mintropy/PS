"""
Title : 상어 초등학교
Link : https://www.acmicpc.net/problem/21608
"""

import sys
input = sys.stdin.readline


def search(student_idx: int):
    global n, classroom, students_order, students_seat
    global dx, dy
    # 모든 학생의 자리가 정해졌다면
    if student_idx == n ** 2 + 1:
        # 만족도 조사
        happiness = 0
        for student, *friends in students_order[1:]:
            # 인접 자리 친구
            friends_near_count = 0
            student_pos = students_seat[student]
            for f in friends:
                if abs(student_pos[0] - students_seat[f][0]) + abs(student_pos[1] - students_seat[f][1]) == 1:
                    friends_near_count += 1
            # 인접 친구 수에 따라 점수 부여
            if friends_near_count == 1:
                happiness += 1
            elif friends_near_count == 2:
                happiness += 10
            elif friends_near_count == 3:
                happiness += 100
            elif friends_near_count == 4:
                happiness += 1000
        return happiness
    # 아니라면 다음 학생자리 찾기
    prob_happiness = 0
    student, *friends = students_order[student_idx]
    # 이미 자리가 정해진 친구가 있는지 없는지 탐색
    # 있다면, 인접해서 앉을 수 있는지 확인하고 자리 정해주기
    # 없다면 가장 왼쪽, 위부터 탐색, 인접 자리가 가장 많이 비어있는 자리로 배정
    friends_already_seated = []
    for f in friends:
        if students_seat[f] != []:
            friends_already_seated.append(students_seat[f])
    # 자리에 앉은 친구가 있는 경우
    if friends_already_seated != []:
        # 자리에 앉은 친구 모두가 인접한 자리가 가능한지 >> 인접친구 0명까지 탐색
        prob_seat = []
        for x, y in friends_already_seated:
            # 4방향 탐색 
            if x > 0 and classroom[x - 1][y] == 0:
                prob_seat.append((x - 1, y))
            if x < n - 1 and classroom[x + 1][y] == 0:
                prob_seat.append((x + 1, y))
            if y > 0 and classroom[x][y -1 ] == 0:
                prob_seat.append((x, y - 1))
            if y < n - 1 and classroom[x][y + 1] == 0:
                prob_seat.append((x, y + 1))
        # 주변 친구수에 따른 자리
        # 주변의 빈자리가 몇개인지 확인 필요 / 가장 빈자리 많은 곳으로 배치
        friends_near = 0
        max_prob_seat = []
        for i in range(len(prob_seat)):
            same_seat_count = 0
            for j in range(i + 1, len(prob_seat)):
                if prob_seat[i] == prob_seat[j]:
                    same_seat_count += 1
            if same_seat_count > friends_near:
                friends_near = same_seat_count
                max_prob_seat = [prob_seat[i]]
            elif same_seat_count == friends_near:
                max_prob_seat.append(prob_seat[i])
        # 가능한 주변 자리를 모두 탐색
        for x, y in max_prob_seat:
            # 학생 배치 후 탐색 >> 탐색 후 제거
            classroom[x][y] = student
            students_seat[student] = [x, y]
            happy = search(student_idx + 1)
            classroom[x][y] = 0
            students_seat[student] = []
            if happy > prob_happiness:
                prob_happiness = happy
    # 자리에 앉은 친구가 없는 경우
    else:
        prob_seat = []
        empty_seat = 0
        for i in range(n):
            if empty_seat == 4:
                break
            for j in range(n):
                # 4방향 탐색
                empty = 0
                if i > 0 and classroom[i - 1][j] == 0:
                    empty += 1
                if i < n - 1 and classroom[i + 1][j] == 0:
                    empty += 1
                if j > 0 and classroom[i][j - 1] == 0:
                    empty += 1
                if j < n - 1 and classroom[i][j + 1] == 0:
                    empty += 1
                if empty == 4:
                    prob_seat = [i, j]
                    empty_seat = 4
                    break
                elif empty > empty_seat:
                    prob_seat = [i, j]
                    empty_seat = empty
        # 학생 배치 후 탐색 >> 탐색 후 제거
        classroom[prob_seat[0]][prob_seat[1]] = student
        students_seat[student] = prob_seat
        prob_happiness = search(student_idx + 1)
        classroom[prob_seat[0]][prob_seat[1]] = 0
        students_seat[student] = []
    return prob_happiness


n = int(input())
# 학생 자리 배치 순서
students_order = [()] + [tuple(map(int, input().split())) for _ in range(n ** 2)]
# 각 학생의 자리
students_seat = [[] for _ in range(n ** 2 + 1)]
# 교실
classroom = [[0] * n for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

print(search(1))
