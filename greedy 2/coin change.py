coins = [1,2,5]
amount = 11
# Output: 3


def solve(coins, amount) :
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for a in range(1,amount+1) :
        for c in coins :
            if a-c >= 0 :
                dp[a] = min(dp[a] , 1+dp[a-c])

    if dp[amount] == float('inf') :
        return -1
    else :
        return dp[amount]
print(solve(coins,amount))