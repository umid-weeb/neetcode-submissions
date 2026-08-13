from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for key in strs:
            keys = "".join(sorted(key))
            group[keys].append(key)

        return list(group.values())