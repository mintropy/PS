"""
Title : 고스택
Link : https://www.acmicpc.net/problem/3425
"""

import sys
input = sys.stdin.readline


def get_input() -> list:
    commands = []
    while True:
        cmd = input().strip()
        if cmd == 'END':
            return commands
        if cmd == 'QUIT':
            return ['QUIT']
        commands.append(cmd)


while True:
    commands = get_input()
