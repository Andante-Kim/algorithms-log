s = input()

def logestPalindrome(s):
    l_list = {}
    count  = 0
    even_count = 0
    odd_count = 0

    if len(s) == 1:
        output = 1
    else:
        for letter in s:
            if letter in l_list:
                l_list[letter] += 1
            else:
                l_list[letter] = 1
        
        for alpha in l_list:
            num = l_list[alpha]
            
            even_count += (num // 2) * 2
            odd_count += num % 2

        odd_count = 1 if odd_count > 0 else 0
        output = even_count + odd_count
    return output

print(logestPalindrome(s))