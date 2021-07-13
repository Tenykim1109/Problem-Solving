def maxSumDivThree(nums):
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(3)]
        dp[nums[0] % 3][0] = nums[0]
        for i in range(1, n):
            for r in range(3):
                print((r - nums[i])%3)
                include = dp[(r - nums[i]) % 3][i-1] + nums[i]
                print(include)
                if include % 3 == r:
                    dp[r][i] = max(dp[r][i-1], include)
                else:
                    dp[r][i] = dp[r][i-1]
        print(dp)
        return dp[0][n-1]
        

print(maxSumDivThree([3, 6, 5, 1, 8]))