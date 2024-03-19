class Solution:
    def isHappy(self, n: int) -> bool:
        # Solution 1:
        # visited is the numbers which we have already encountered while
        # calculating the sum of squares of a number
        visited = set()

        # helper function to calculate the sum of squares of the digits
        def sumOfSquares(n: int) -> int:
            output = 0
        
            while n:
                # getting the last digit
                digit = n % 10
                output += digit ** 2
                # getting rid of the last digit
                n = n // 10

            return output

        while n not in visited:
            visited.add(n)

            n = sumOfSquares(n)

            if n == 1:
                return True

        return False

