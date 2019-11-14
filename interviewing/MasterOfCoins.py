
def register(cents):
    coins = 0
    drawer = [25, 10, 5, 1]
    for coin in drawer:
        coins_added = int(cents/coin)
        coins += coins_added
        cents = cents%coin
    print(coins)
    return coins

if __name__ == '__main__':
    register(30)