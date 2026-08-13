from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for str_ in strs:
            counter = Counter(str_)
            key = frozenset(counter.items())
            group[key].append(str_)

        return list(group.values())