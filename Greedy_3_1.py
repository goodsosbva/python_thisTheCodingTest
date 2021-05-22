n = 1260
count = 0
i = 0

list = [500,100,50,10]

for coin in list:
    count += n // coin
    i = i + 1
    print("[",i,"]:",count)
    n %= coin

print("결과:",count)