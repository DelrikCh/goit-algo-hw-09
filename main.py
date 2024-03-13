import time


def find_coins_greedy(amount, coins):
    coins.sort(reverse=True)
    result = {}
    for coin in coins:
        num_coins = amount // coin
        amount -= num_coins * coin
        result[coin] = num_coins
    return result


def find_min_coins(amount, coins):
    coins.sort()
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    result = {}
    for coin in reversed(coins):
        num_coins = amount // coin
        amount -= num_coins * coin
        result[coin] = num_coins

    return result


def main():
    coins = [1, 2, 5, 10, 25, 50]
    large_amount = 9128360

    start_time_greedy = time.time()
    result_greedy = find_coins_greedy(large_amount, coins)
    end_time_greedy = time.time()
    time_greedy = end_time_greedy - start_time_greedy

    start_time_dp = time.time()
    result_dp = find_min_coins(large_amount, coins)
    end_time_dp = time.time()
    time_dp = end_time_dp - start_time_dp

    # Виводимо результати
    print("Жадібний алгоритм:")
    print("Час виконання:", time_greedy)
    print("Результат:", result_greedy)
    print()

    print("Алгоритм динамічного програмування:")
    print("Час виконання:", time_dp)
    print("Результат:", result_dp)


if __name__ == '__main__':
    main()
