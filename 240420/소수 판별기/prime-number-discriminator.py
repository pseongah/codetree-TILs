n = int(input())
prod = 1

for i in range(2, n+1):
    if n % i == 0:
        prod += 1

if prod == 2:
    print("P")
else:
    print("C")