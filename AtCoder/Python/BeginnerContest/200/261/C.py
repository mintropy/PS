N = int(input())
files = {}

for _ in range(N):
    file_name = input().strip()
    if file_name in files:
        count = files[file_name]
        files[file_name] += 1
        print(f"{file_name}({count})")
    else:
        files[file_name] = 1
        print(file_name)
