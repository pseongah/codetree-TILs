n = int(input())
sum_val = 0

for _ in range(n):
    n = int(input())
    if n % 2 == 1 and n % 3 == 0:
        sum_val += n
print(sum_val)