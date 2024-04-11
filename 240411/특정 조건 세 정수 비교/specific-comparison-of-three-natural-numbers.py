a, b, c = map(int, input().split())

if a <= b and a <= c:
    case1 = 1
else:
    case1 = 0

if a == b == c:
    case2 = 1
else:
    case2 = 0

print(case1, case2)