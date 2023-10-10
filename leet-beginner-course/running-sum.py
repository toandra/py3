class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        results = []
        results.append(nums[0])

        index = 1
        end = len(nums)

        # input list example: (1,2,3,4)
      
        for num in nums:
            if index < end:
                results.append( nums[index] + results[index - 1] )
                index += 1

        # output result should be: (1,3,6,10)
        return results
    
print(Solution().runningSum([1,2,3,4]))
