def findMin(n):
    coins = [1,2,5,10]
    remain = n
    count = 0
    ptr = len(coins)-1
    while remain >= 0:
        if remain == 0:
            break
        if coins[ptr] > remain:
            ptr -= 1
            continue
        remain -= coins[ptr]
        count += 1 
    return count

print(findMin(24))