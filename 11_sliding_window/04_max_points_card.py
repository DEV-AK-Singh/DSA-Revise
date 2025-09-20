def maxScore(cardPoints, k):
    n = len(cardPoints)
    if n == k:
        return sum(cardPoints)
    maxi = 0
    ls = 0
    rs = 0
    rindex = n-1
    for i in range(0, k):
        ls += cardPoints[i]
    maxi = ls
    for i in range(k-1, -1, -1):
        ls -= cardPoints[i]
        rs += cardPoints[rindex]
        maxi = max(maxi, ls+rs)
        rindex -= 1
    return maxi
        
