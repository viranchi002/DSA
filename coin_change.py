import sys


def coin_change(coins, m, s):
    table = [0 for _ in range(0, s + 1)]
    table[0] = 0
    for i in range(1, s + 1):
        table[i] = sys.maxsize
    print(table)

    for i in range(1, s + 1):
        for j in range(m):
            if coins[j] <= i:
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                        sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    if table[s] == sys.maxsize:
        return -1
    return table[s]


if __name__ == '__main__':
    coins = [9, 6, 5, 1]
    m = len(coins)
    print(coin_change(coins, m, 11))
