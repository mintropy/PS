import sys
input = sys.stdin.readline


if __name__ == "__main__":
    A, B = map(int, input().split())
    if A == 0:
        print(0, 1)
    elif B == 0:
        print(1, 0)
    else:
        t = (1 / (1 + (B * B) / (A * A))) ** 0.5
        print(t, (B / A) * t)