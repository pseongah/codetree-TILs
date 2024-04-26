arr = list(map(int, input().split()))
k = 0

for i in arr:
    k += 1
    if i % 3 == 0:
        break

print(arr[k-2])