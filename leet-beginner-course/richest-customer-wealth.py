class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:

        results = []
        largest = 0
        
        for account_index, account in enumerate(accounts): 
            total = 0
            for wealth_index, wealth in enumerate(account): 
                total += accounts[account_index][wealth_index]  
            results.append(total)

        for result in results: 
            if largest == 0: 
                largest = result
            if largest < result:
                largest = result

        return largest


print(Solution().maximumWealth([[1,2,3],[12,1,22],[2,2,2]]))