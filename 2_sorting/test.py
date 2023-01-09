num = int(input())
teams = [(n, [int(i) for i in input().split()]) for n in range(1, num + 1)]
teams = sorted(teams, key=lambda tup: (-tup[1][0], tup[1][1]))
if len(set([item[1][1] for item in teams])) == 1:
    print(" ".join([str(i) for i in sorted([sample[0] for sample in teams])]))
else:
    print(" ".join([str(i) for i in [sample[0] for sample in teams]]))
