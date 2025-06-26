class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n

    # Build prefix product
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
                                                                #time: O(n^2) 
                                                                #space: O(1)
    # Build suffix product
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

    # Final result = prefix * suffix
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result
