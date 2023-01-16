n = int(input())
strings = [input() for _ in range(n)]
for s in strings:
    m = min(s.count("0"), s.count("1"))
    if m % 2 == 1:
        print("DA")
    else:
        print("NET")
