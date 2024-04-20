while True:
    w, h, s = map(str, input().split())

    print(int(w)*int(h))
    if s == "C":
        break