n = int(input())
cnt = 0
student1 = list(map(int, input().split()))
student2 = list(map(int, input().split()))
student3 = list(map(int, input().split()))

if sum(student1)/4 >= 60:
    print("pass")
    cnt += 1
else:
    print("fail")
if sum(student2)/4 >= 60:
    print("pass")
    cnt += 1
else:
    print("fail")
if sum(student3)/4 >= 60:
    print("pass")
    cnt += 1
else:
    print("fail")
print(cnt)