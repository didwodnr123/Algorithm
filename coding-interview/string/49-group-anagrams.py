import collections
from typing import List, Any


def group_anagrams(strs: List[str]):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()
