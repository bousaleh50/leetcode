class Solution:
    def reverse(self, x: int) -> int:
        rev_number = int(str(x)[::-1]) if str(x)[0]!="-" else -int(str(x)[:0:-1])

        return 0 if (rev_number>((2**31)-1) or rev_number<(-2**31)) else rev_number

    def reverse2(self,x:int)->int:
        copy_x = abs(x)
        rev_num = 0
        while (copy_x != 0):
            rev_num = (rev_num * 10) + (copy_x % 10)
            copy_x //= 10
        rev_num = 0 if (rev_num > ((2 ** 31) - 1) or rev_num < (-2 ** 31)) else rev_num
        return rev_num if x > 0 else -rev_num

