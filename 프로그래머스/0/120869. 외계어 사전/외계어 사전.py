from itertools import permutations

def solution(spell, dic):
    k = list(permutations(''.join(spell), len(spell)))
    for i in k:
        if ''.join(i) in dic:
            return 1
            break
    return 2