def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    n = 0
    while 10 ** n <= x:
        n += 1
    for i in range(n // 2):
        a = x % 10 ** (i + 1) // 10 ** i
        b = x // 10 ** (n - i - 1) % 10
        if a != b:
            return False
    return True


print(isPalindrome(12344321))
