arr_n = list(map(int, input().split()))
sum_val = 0
cnt = 0

for i in arr_n:
    if i == 0:
        break
    sum_val += i
    cnt += 1

print(f"{sum_val} {sum_val/cnt:.1f}")