class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        a = [''] * numRows
        up = False
        current = numRows - 1
        for i in range(len(s)):
            if not up and current == 0:
                up = True
            elif up and current == numRows - 1:
                up = False

            a[current] += s[i]

            if up:
                current += 1
            else:
                current -= 1
        return ''.join(a[::-1])
