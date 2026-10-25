class Solution:
    def climbStairs(self, n: int) -> int:

        dp = {}

        def climbStairs_recur(n):
            if n < 0:
                return 0
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 2
            
            # number of ways to jump from 
            if n in dp:
                return dp[n]
            dp[n] = climbStairs_recur(n-1) + climbStairs_recur(n-2)
            return dp[n]
            
        return climbStairs_recur(n)
        