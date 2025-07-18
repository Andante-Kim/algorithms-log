class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        # s.lengh <= 2
        if len(s) <= 2:
            return True
        
        # s.lengh >= 2
        # check Palindrome
        reverse_s = s[::-1]
        if reverse_s == s:
            return True
        
        # if it need to delete someting
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
            left += 1
            right -= 1
        
        return True

# 사용자가 입력한 문자열로 실행
if __name__ == "__main__":
    s = input("검사할 문자열을 입력하세요: ")
    sol = Solution()
    result = sol.validPalindrome(s)
    print(result)