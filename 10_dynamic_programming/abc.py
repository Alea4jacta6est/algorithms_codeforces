def get_occurencies(line, substring, major_len, minor_len):
    if minor_len == 0:
        return 1
    if major_len == 0:
        return 0
    if line[major_len - 1] == substring[minor_len - 1]:
        return get_occurencies(
            line, substring, major_len - 1, minor_len - 1
        ) + get_occurencies(line, substring, major_len - 1, minor_len)
    else:
        return get_occurencies(line, substring, major_len - 1, minor_len)


line = input()
counter, grouped = {i: 0 for i in ["a", "c"]}, []
for char in line:
    if char == "a":
        counter["a"] += 1
    if char == "c":
        counter["c"] += 1
    if char == "b":
        grouped.append((counter["a"], counter["c"]))
print(sum(a * (counter["c"] - c) for a, c in grouped))
