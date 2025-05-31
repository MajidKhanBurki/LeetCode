class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # negative numbers can't be palindromes

        res = list(map(int, str(x)))
        left = 0
        right = len(res) - 1

        while left <= right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1

        return True
