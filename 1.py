import time
from collections import defaultdict

# Набір монет
COINS = [50, 25, 10, 5, 2, 1]

# Жадібний алгоритм
def find_coins_greedy(amount):
    result = defaultdict(int)
    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
    return dict(result)

# Динамічне програмування
def find_min_coins(amount):
    # Набір монет
    coins = COINS
    # Масив для зберігання найменшої кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    # Для суми 0 потрібно 0 монет
    dp[0] = 0
    # Масив для відстеження монет, що використовуються
    used_coins = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[i] = coin

    # Відновлення використовуваних монет
    result = defaultdict(int)
    while amount > 0:
        coin = used_coins[amount]
        result[coin] += 1
        amount -= coin

    return dict(result)

# Порівняння ефективності
def compare_algorithms(amount):
    # Жадібний алгоритм
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time
    
    # Динамічне програмування
    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time
    
    print(f"Жадібний алгоритм: {greedy_result}, час: {greedy_time:.6f} секунд")
    print(f"Динамічне програмування: {dp_result}, час: {dp_time:.6f} секунд")

# Приклади використання
amount = 22237658
print("Сума:", amount)
print("Жадібний алгоритм:", find_coins_greedy(amount))
print("Динамічне програмування:", find_min_coins(amount))

# Порівняння ефективності для великих сум
large_amount = 10000
compare_algorithms(large_amount)
