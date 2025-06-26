class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for n in nums:
            if n in hashset:        # time complexity: O(n)
                return True         # space complexity: O(n)
            hashset.add(n)
        return False

        
