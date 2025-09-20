val = [60, 100, 120]
wt = [10, 20, 30] 
capacity = 50

def fractionalKnapsack(val, wt, capacity):
    n = len(val)
    items = [(val[i], wt[i]) for i in range(0, n)]
    items.sort(key=lambda item: item[0]/item[1], reverse=True)
    total_val = 0
    total_wt = 0
    ptr = 0
    for val, wt in items:
        if total_wt + wt <= capacity:
            total_val += val
            total_wt += wt
        else:
            remain = capacity - total_wt
            if remain <= 0:
                break
            total_val += (remain * (val/wt))
            break
    return total_val

print(fractionalKnapsack(val, wt, capacity))