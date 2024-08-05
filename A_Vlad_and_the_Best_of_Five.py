for _ in range(int(input())):
    x = 0
    s = input()
    for i in s:
        if i == "A":
            x += 1
        else:
            x -= 1
    print("A" if x > 0 else "B")