n_arr = list(map(int, input().split()))
sum_val = 0
cnt = 0

for i in n_arr:
    if i >= 250:
        break
    sum_val += i
    cnt += 1
print(f"{sum_val} {sum_val/cnt:.1f}")