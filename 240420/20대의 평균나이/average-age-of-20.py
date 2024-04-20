sum_val, cnt = 0, 0

while True:
    age = int(input())
    if age >= 30:
        break
    else:
        sum_val += age
        cnt += 1

# print(f"{sum/cnt:.2f}")
print("%.2f" %(sum_val/cnt))