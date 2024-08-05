for _ in range(int(input())):
    sorted_numbers = sorted(list(map(int, input().split())))
    if (sorted_numbers[0] + sorted_numbers[1]) == sorted_numbers[2]:
        print("YES")
    else:
        print("NO")