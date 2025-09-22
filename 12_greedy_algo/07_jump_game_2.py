jumps = [2,3,1,1,4] 

def canJump(jumps):
    n = len(jumps)
    l = 0
    r = 0
    jumps_count = 0
    while r < n-1:
        farthest = 0
        for i in range(l, r+1):
            farthest = max(farthest, i+jumps[i])
        l = r+1
        r = farthest
        jumps_count += 1
    return jumps_count

print(canJump(jumps))    
    
