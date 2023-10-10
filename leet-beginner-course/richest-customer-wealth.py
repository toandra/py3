class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:

        results = []
        most_biggly = 0
        
        for account in accounts: 
            total = 0
            for wealth in account: 
                total += wealth  
            results.append(total)

        for result in results: 
            if most_biggly == 0: 
                most_biggly = result
            if most_biggly < result:
                most_biggly = result

        return most_biggly


print(Solution().maximumWealth([[1,2,3],[12,1,22],[2,2,2]]))