degree = int(input())

if degree < 0:
    print("ice")
elif 0 <= degree < 100:
    print('water')
else:
    print('vapor')