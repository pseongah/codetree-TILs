arr = list(map(int, input().split()))

even_arr = arr[1:10:2]
third_arr = []
# print(even_arr)

for i in range(2, 10, 3):
    third_arr.append(arr[i])

print(sum(even_arr), end=' ')
third_sum = sum(third_arr)/len(third_arr)
print(f"{third_sum:.1f}")