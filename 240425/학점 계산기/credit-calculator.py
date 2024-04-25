n = int(input())
arr_score = list(map(float, input().split()))

avg = sum(arr_score)/n
print(f"{avg:.1f}")

if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor.0")