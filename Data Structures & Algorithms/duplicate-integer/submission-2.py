class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        if not nums:
            return False
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        
        