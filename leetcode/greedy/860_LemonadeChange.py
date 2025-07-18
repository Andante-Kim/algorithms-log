def lemonadeChange(bills):
    my_pocket = {
        5 : 0,
        10 : 0,
        20 : 0
    }
    
    for customer in bills:
        if customer == 5:
            my_pocket[5] += 1
        elif customer == 10:
            if my_pocket[5] > 0:
                my_pocket[5] -= 1
                my_pocket[10] += 1
            else:
                return False
        else:
            if my_pocket[5] > 0 and my_pocket[10] > 0:
                my_pocket[5] -= 1
                my_pocket[10] -= 1
            elif my_pocket[5] >= 3:
                my_pocket[5] -= 3
            else:
                return False
    return True

bills = list(map(int, input().split()))
print(lemonadeChange(bills))