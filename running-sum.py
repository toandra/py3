from ast import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        results = []
        results.append(nums[0])

        index = 1
        end = len(nums)

        for num in nums:
            if index < end:
                results.append( nums[index] + results[index - 1] )
                index += 1

        return results
