n = int(input())
arr = list(map(int, input().split()))

# new_arr = []

# new_arr.append(elem * elem for elem in arr)

for i in arr:
    print(i*i, end=' ')