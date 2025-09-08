class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s = ''
        while a > 0 and b > 0:
            if a == b:
                s = s + 'a' * 1 + 'b' * 1
                a = a - 1
                b = b - 1
            elif a > b:
                s = s + 'a' * 2 + 'b' * 1
                a = a - 2
                b = b - 1
            else:
                s = s + 'b' * 2 + 'a' * 1
                a = a - 1
                b = b - 2
        if a > 0:
            s = s + 'a' * a
        elif b > 0:
            s = s + 'b' * b

        return s