def lemonadeChange(bills):
    fs = 0
    ts = 0
    for bill in bills:
        if bill == 5:
            fs += 1
        elif bill == 10:
            if fs >= 1:
                fs -= 1
                ts += 1 
            else:
                return False
        else:
            if fs >= 1 and ts >= 1:
                fs -= 1
                ts -= 1
            elif fs >= 3:
                fs -= 3 
            else:
                return False 
    return True

bills = [5,5,10,5,20,5,5,5,5,5,20,5,10,5,5,5,5,20,20,5]

print(lemonadeChange(bills))