def brackets(bracket_sequence):
    def match(b1, b2):
        brackets = {"{": "}", "(": ")", "[": "]"}
        return b1 in brackets and brackets[b1] == b2

    arr = [[0] * len(bracket_sequence) for _ in range(len(bracket_sequence))]
    for i in range(len(bracket_sequence)):
        arr[i][i] = 0
    for i in range(len(bracket_sequence) - 1):
        arr[i][i + 1] = int(match(bracket_sequence[i], bracket_sequence[i + 1])) * 2
    for len_ in range(3, len(bracket_sequence) + 1):
        for i in range(0, len(bracket_sequence) - 2):
            j = i + len_ - 1
            if j < len(bracket_sequence):
                if match(bracket_sequence[i], bracket_sequence[j]):
                    arr[i][j] = arr[i + 1][j - 1] + 2
                else:
                    arr[i][j] = arr[i + 1][j - 1]
                for k in range(i, j):
                    arr[i][j] = max(arr[i][j], arr[i][k] + arr[k + 1][j])
    return arr[0][len(bracket_sequence) - 1]


print(brackets(input()))
