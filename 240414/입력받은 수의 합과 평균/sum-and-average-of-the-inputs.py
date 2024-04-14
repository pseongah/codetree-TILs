n = int(input())
sum_val = 0

for _ in range(n):
    num = int(input())
    sum_val += num

print(sum_val, "%.1f" %(sum_val/n))