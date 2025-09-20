def totalFruit(fruits):
    l = 0
    r = 0
    basket = dict()
    maxi = 0
    n = len(fruits)
    while r < n: 
        basket[fruits[r]] = basket.get(fruits[r],0)+1
        if len(basket) > 2:
            basket[fruits[l]] -= 1
            if basket[fruits[l]] == 0:
                del basket[fruits[l]] 
            l += 1 
        if len(basket) <= 2:
            maxi = max(maxi, r-l+1)
        r += 1
    return maxi
 
