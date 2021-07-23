'''
Title : 리모컨
Link : https://www.acmicpc.net/problem/1107
'''

import sys

input = sys.stdin.readline

def plus_to_channel(m, alive):
    global channel
    count = 0
    if len(channel) == 1:
        want = int(channel[0])
        if alive[0] > want:
            return int(1e6)
        else:
            min_of_max = alive[0]
            for button in alive:
                if button <= want:
                    min_of_max = button
            return want - button
    else:
        channel_num = int(''.join(channel))
        # 같은 자리수 중 더 작은값이 있는지
        if alive[0] == 0:
            min_button_none_zero = alive[1]
        else:
            min_button_none_zero = alive[0]
        # 채널과 같은 자리수로 만들 수 있는지
        if min_button_none_zero <= int(channel[0]):
            # 같은 자리수 일 때
            new_channel_length = len(channel)
            new_channel = 0
            # 코드 추가하기
            pass

        else:
            # 하나 짧은 자리수일 때
            new_channel_length = len(channel) - 1
            new_channel = alive[-1]
            for _ in range(new_channel_length - 1):
                new_channel *= 10
                new_channel += alive[-1]
            return channel_num - new_channel
    


channel = list(input().strip())
m = int(input())
broken = list(map(int, input().split()))
alive = list(range(0, 10))
alive = list(set(alive) - set(broken))

# 100번부터 +, - 버튼만으로 이동
count_only_plus_minus = abs(channel - 100)
if m == 10:
    print(count_only_plus_minus)
else:
    # 숫자버튼으로 이동 후, +, - 버튼으로 이동하는 회수
    count_num_plus = plus_to_channel(m, broken)