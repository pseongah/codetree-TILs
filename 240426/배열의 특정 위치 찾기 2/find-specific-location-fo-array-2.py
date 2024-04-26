arr = list(map(int, input().split()))

even_arr = arr[1:9:2]
odd_arr = arr[0:9:2]

even_sum = sum(even_arr)
odd_sum = sum(odd_arr)

print(even_sum - odd_sum if even_sum >= odd_sum else odd_sum - even_sum)