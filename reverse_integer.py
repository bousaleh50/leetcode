class Solution:
    def reverse(self, x: int) -> int:
        rev_number = int(str(x)[::-1]) if str(x)[0]!="-" else -int(str(x)[:0:-1])

        return 0 if (rev_number>((2**31)-1) or rev_number<(-2**31)) else rev_number