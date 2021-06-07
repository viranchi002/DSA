# remember set theory
# suppose we want to look for the number of ways for 5 using [1,2]
# we will check number of ways for 5-1 and 5-2 and add 1 and 2 respectively to the total number of ways as there will
# never be common elements
# number of ways for 5-1 = 4 => {1,1,1,1}, {1,2,1}, {2,2} : now adding 1 will make {1,1,1,1,1},{1,2,1,1},{2,2,1}
# number of ways for 5-2 = 3 => {1,1,1}.{1,2} : now adding 2 will make {1,1,1,2}, {1,2,2} and notice how all 5 sets are
# different
def change_ways(coins, m, s):
    table = [0 for _ in range(s + 1)]
    table[0] = 1
    for i in range(0, m):
        for j in range(coins[i], s + 1):
            table[j] += table[j - coins[i]]
    return table[s]


if __name__ == "__main__":
    coins = [1, 2, 3]
    m = len(coins)
    s = 4
    print("Maximum ways",
          change_ways(coins, m, s))
