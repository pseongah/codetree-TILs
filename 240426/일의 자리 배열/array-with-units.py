a, b = map(int, input().split())

arr = [0, a, b, 0, 0, 0, 0, 0, 0, 0, 0]
print(a, b, end=' ')
for i in range(3, 11):
    arr[i] = (arr[i-1]+arr[i-2]) % 10
    print(arr[i], end=' ')