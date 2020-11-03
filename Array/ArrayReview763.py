# Array 763
""" string with letters, partition this string inro as many as possible so that each letter appears
in at most one part, and return a list of integers representing the size of these parts"""
from collections import defaultdict
def partition_labels(S):
    result = []
    position = defaultdict(int)
    for i, le in enumerate(S):
        position[le] = i
    last_chunk = -1
    max_cnt = 0
    for j in range(len(S)):
        curr = S[j]
        max_cnt = max(max_cnt, position[curr])
        if max_cnt ==j:
            result.append(j - last_chunk)
            last_chunk = j
    return result
