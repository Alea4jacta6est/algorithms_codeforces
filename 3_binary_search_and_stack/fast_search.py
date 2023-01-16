import bisect


def fast_search(array, queries):
    sorted_array = sorted(array)
    responses = [0] * len(queries)
    for i, request in enumerate(queries):
        left = bisect.bisect_left(sorted_array, request[0])
        right = bisect.bisect_right(sorted_array, request[1])
        responses[i] = right - left
    return responses


array_length = int(input())
array = [int(i) for i in input().split()]
queries_number = int(input())
queries = [[int(x) for x in input().split()] for _ in range(queries_number)]
responses = fast_search(array, queries)
print(" ".join(str(i) for i in responses))
"""5
10 1 10 3 4
4
1 10
2 9
3 4
2 2"""
