arr = list(map(int, input().split()))
new_arr = []

for i in arr:
    if i == 0:
        break
    new_arr.append(i)
reversed_arr = new_arr[::-1]

for elem in reversed_arr:
    print(elem, end=" ")