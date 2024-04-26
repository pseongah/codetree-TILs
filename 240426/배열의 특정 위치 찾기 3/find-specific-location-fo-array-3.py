arr = list(map(int, input().split()))
cnt = 0
sum_val = 0

for i in arr:
    cnt += 1
    if i == 0:
        break

sum_val = arr[cnt-4]+arr[cnt-2]+arr[cnt-3]
print(sum_val)