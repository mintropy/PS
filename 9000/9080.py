"""
Title : PC방 요금
Link : https://www.acmicpc.net/problem/9080 
"""

import sys
input = sys.stdin.readline

'''
for _ in range(int(input())):
    st_time, duration = input().strip().split()
    # 시간 시간, 분
    st_h, st_m = map(int, st_time.split(':'))
    # 총 사용 시간
    duration = int(duration)
    
    fee = 0
    while duration:
        # 야간 시간
        if st_h == 22 and st_m == 0:
            # 남은 시간이 5시간 이상일 때와 아닐때로
            if duration >= 60 * 5:
                fee += 5000
                if duration >= 60 * 10:
                    st_h = 8
                    duration -= 60 * 10
                else:
                    break
            else:
                if duration % 60:
                    duration //= 60
                    duration += 1
                else:
                    duration //= 60
                fee += duration * 1000
                break
        # 주간 시작
        elif st_h == 8 and st_m == 0:
            # 전체 남은 사용 시간이 5시간 이하인 경우
            if duration <= 60 * 5:
                if duration % 60:
                    duration //= 60
                    duration += 1
                else:
                    duration //= 60
                fee += duration * 1000
                break
            # 주간을 풀로 채울 수 있을 때
            if duration >= 14 * 60:
                fee += 14 * 1000
                st_h = 22
                duration -= 14 * 60
            else:
                if duration % 60:
                    duration //= 60
                    duration += 1
                else:
                    duration //= 60
                fee += duration * 1000
                break
        # 주간
        elif 8 <= st_h < 22:
            # 전체 남은 사용 시간이 5시간 이하인 경우
            if duration <= 60 * 5:
                if duration % 60:
                    duration //= 60
                    duration += 1
                else:
                    duration //= 60
                fee += duration * 1000
                break
            # 야간 시작 까지 남은 시간
            left_time = (21 - st_h) * 60 + (60 - st_m)
            if duration >= left_time:
                if left_time % 60:
                    fee += ((left_time // 60) + 1) * 1000
                else:
                    fee += (left_time // 60) * 1000
                st_h = 22
                st_m = 0
                duration -= left_time
            else:
                if duration % 60:
                    duration //= 60
                    duration += 1
                else:
                    duration //= 60
                fee += duration * 1000
                break
        # 야간
        else:
            # 주간 시간 까지 남은 시간
            if st_h >= 22:
                left_time = 60 * 8 + (23 - st_h) * 60 + (60 - st_m)
            else:
                left_time = (7 - st_h) * 60 + (60 - st_m)
            # 남은 시간이 5시간 이상일 때와 아닐때로
            if duration >= 60 * 5 and left_time >= 60 * 5:
                fee += 5000
                if duration - left_time >= 0:
                    st_h = 8
                    st_m = 0
                    duration -= left_time
                else:
                    break
            else:
                if left_time >= duration:
                    if duration % 60:
                        duration //= 60
                        duration += 1
                    else:
                        duration //= 60
                    fee += duration * 1000
                    break
                else:
                    if left_time % 60:
                        left_time //= 60
                        left_time += 1
                    else:
                        left_time //= 60
                    fee += left_time * 1000
                    break
    print(fee)
'''


'''
1
20:59 361

'''
