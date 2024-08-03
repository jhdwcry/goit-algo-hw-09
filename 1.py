def find_coins_greedy(amount, set=[50, 25, 10, 5, 2, 1]):
    coins = {}
    for coin in set:
        count = amount // coin
        if count > 0:
            coins[coin] = count
        amount -= coin * count
    return coins

def find_min_coins(amount, set=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  

    coins_used = [0] * (amount + 1)

    for coin in set:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coins_used[i] = coin

    coins = {}
    while amount > 0:
        coin = coins_used[amount]
        if coin in coins:
            coins[coin] += 1
        else:
            coins[coin] = 1
        amount -= coin

    return coins

result_greedy = find_coins_greedy(113)
print(result_greedy)  

result_dp = find_min_coins(113)
print(result_dp) 
