class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        n = 1
        d = abs(x)
        sign = x < 0
        while True:
            d //= 10
            if d == 0:
                break
            n += 1
        d = abs(x)
        for i in range(n):
            a = 10 * a + d % 10
            d //= 10
        res = sign and -a or a
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        return res
