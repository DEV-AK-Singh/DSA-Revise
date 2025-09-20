def findContentChildren(g, s):
    g.sort()
    n = len(g)
    s.sort()
    m = len(s)
    i = 0
    j = 0
    count = 0
    while j < m and i < n:
        if g[i] <= s[j]:
            i += 1
            count += 1
        j += 1
    return count