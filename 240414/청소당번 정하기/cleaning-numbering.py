cnt_room, cnt_wall, cnt_toilet = 0, 0, 0

n = int(input())

for i in range(1, n+1):
    if i % 12 == 0:
        cnt_toilet += 1
    elif i % 3 == 0:
        cnt_wall += 1
    elif i % 2 == 0:
        cnt_room += 1

print(cnt_room, cnt_wall, cnt_toilet)