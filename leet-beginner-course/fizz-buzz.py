class Solution: 
    def fizzBuzz(self, num: int) -> list[str]:
      results = []
      for i in range(1, num+1):
         if i % 3 == 0 and i % 5 == 0: 
            results.append("FizzBuzz")
         elif i % 5 == 0: 
            results.append("Buzz")
         elif i % 3 == 0: 
            results.append("Fizz")
         else: 
            results.append(str(i))

      return results
    
print(Solution().fizzBuzz(3))
print(Solution().fizzBuzz(5))
print(Solution().fizzBuzz(15))