"""
Title : 줄서기
Link : https://www.acmicpc.net/problem/17178
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    tickets = []
    for _ in range(N):
        line = list(input().strip().split())
        for ticket in line:
            alp, num = ticket.split("-")
            tickets.append((alp, int(num)))
    tickets_sroted = sorted(tickets, reverse=True)
    stack = []
    for ticket in tickets:
        if ticket == tickets_sroted[-1]:
            tickets_sroted.pop()
            continue
        while stack:
            if stack[-1] == tickets_sroted[-1]:
                stack.pop()
                tickets_sroted.pop()
            else:
                break
        stack.append(ticket)
    else:
        while stack:
            if stack[-1] == tickets_sroted[-1]:
                stack.pop()
                tickets_sroted.pop()
            else:
                break
    if stack:
        print("BAD")
    else:
        print("GOOD")
