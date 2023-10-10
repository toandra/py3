class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:

        results = []
        most_biggly = 0
        
        for account_index, account in enumerate(accounts): 
            total = 0
            for wealth_index, wealth in enumerate(account): 
                total += accounts[account_index][wealth_index]  
            results.append(total)

        for result in results: 
            if most_biggly == 0: 
                most_biggly = result
            if most_biggly < result:
                most_biggly = result

        return most_biggly


print(Solution().maximumWealth([[1,2,3],[12,1,22],[2,2,2]]))