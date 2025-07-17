g = list(map(int, input().split())) # children i
s = list(map(int, input().split())) # cookie j

def findContentChildren(g, s):
    if not s : return 0

    children = g
    cookie = s
    children.sort()
    cookie.sort()

    num_cookies = len(cookie)
    index_cookie = 0
    output = 0

    for i in children:
        while index_cookie < num_cookies and i > cookie[index_cookie]:
            index_cookie += 1
            if index_cookie == num_cookies:
                return  output
        output += 1
        index_cookie += 1
        if index_cookie >= num_cookies:
            return output
    return output

print(findContentChildren(g, s))