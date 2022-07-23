import sys
input = sys.stdin.readline


N, K = map(int, input().split())
employees = list(map(int, input().split()))
employees.sort(reverse=True)

pjt_count = 0
while employees:
    if len(employees) < K:
        break
    
    pass

