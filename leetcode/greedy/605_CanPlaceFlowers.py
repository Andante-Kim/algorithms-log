flowerbed = list(map(int, input().split()))
n = int(input())

def canPlaceFlowers(flowerbed, n):
    '''
    # Mycode
    if n == 0:
        return True
    if len(flowerbed) == 1:
        if flowerbed[0] == 0:
            n -= 1
        if n == 0:
            return True
        return False
    # check flowerbed
    for index in range(len(flowerbed)):
        if index == 0 and flowerbed[index] == 0 and flowerbed[index+1]==0:
            flowerbed[index] += 1
            n -= 1
        elif index == len(flowerbed)-1 and flowerbed[index] == 0 and flowerbed[index-1] == 0:
            flowerbed[index] += 1
            n -= 1
        else:
            if flowerbed[index] == 0 and flowerbed[index-1] == 0 and flowerbed[index+1] == 0:
                flowerbed[index] += 1
                n -= 1
        # use all flowers   
        if n == 0:
            return True
    return False
    '''
    # best code
    if n == 0:
        return True
    
    f = [0] + flowerbed + [0]
    
    for index in range(1, len(f)-1):
        if f[index-1]==0 and f[index] == 0 and f[index+1] == 0:
            f[index] = 1
            n -= 1
        if n == 0:
            return True
    return n <= 0

print(canPlaceFlowers(flowerbed, n))