a, b = 0, 0

for _ in range(10):
    n = int(input())
    if n%3 == 0:
        a += 1
    if n%5==0:
        b += 1
print(a, b)