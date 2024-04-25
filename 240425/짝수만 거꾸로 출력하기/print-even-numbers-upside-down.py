n = int(input())
arr = list(map(int, input().split()))
even_arr = []

for i in arr:
    if i % 2 == 0:
        even_arr.append(i)

rev_even = even_arr[::-1]

for elem in rev_even:
    print(elem, end=' ')