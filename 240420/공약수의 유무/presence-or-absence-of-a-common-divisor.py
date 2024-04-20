a, b = map(int, input().split())
sat = False

for i in range(a, b+1):
    if 1920 % i == 0 or 2880 % i == 0:
        sat = True

if sat:
    print("1")
else:
    print("0")