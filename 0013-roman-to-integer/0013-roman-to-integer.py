class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I':1 , 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        out = roman_map[s[len(s)-1]]
        for i in range(len(s)-2,-1,-1):
            if roman_map[s[i]] >= roman_map[s[i+1]]:
                out += roman_map[s[i]]
            else:
                out -= roman_map[s[i]]
        return out