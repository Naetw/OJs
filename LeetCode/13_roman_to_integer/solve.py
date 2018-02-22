class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'M': (1000, 0), 'D': (500, 1), 'C': (100, 2), 'L': (50, 3), 'X': (10, 4), 'V': (5, 5), 'I': (1, 6)}

        num = 0
        prev = -1
        prev_val = 0
        for i in s:
            val, cur = roman_dict[i]
            if cur < prev:
                num -= 2 * prev_val
                num += val
                prev = -1
                prev_val = 0
            else:
                prev = cur
                prev_val = val
                num += val
        return num
