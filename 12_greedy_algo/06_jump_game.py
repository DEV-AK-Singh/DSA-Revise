jumps = [2,3,1,1,4]

def canJump(jumps):
    maxIdx = 0
    n = len(jumps)
    for i in range(0, n):
        if maxIdx < i:
            return False
        maxIdx = max(jumps[i] + i, maxIdx)
    return True