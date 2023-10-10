class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:

        results = []
        largest = 0
        
        for account_index, account in enumerate(accounts): 
            total = 0

            for wealth_index, wealth in enumerate(account): 
                total += accounts[account_index][wealth_index]
                  
            results.append(total)

        return max(results)


print(Solution().maximumWealth([[1,2,3],[12,1,22],[2,2,2]]))