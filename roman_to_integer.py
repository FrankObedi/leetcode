class Solution:
    def reomanToInt(self, s):
        # hashtable of roman symbols and correspoding values
        symbols = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        value = 0
        i = 0
        symbol_count = len(s)

        while i < symbol_count:
            if i < symbol_count-1 and symbols[s[i]] < symbols[s[i+1]]:
                value += symbols[s[i+1]] - symbols[s[i]]
                i += 2
            else:
                value += symbols[s[i]]
                i += 1
        
        return value
    

s = Solution()

print(s.reomanToInt("XXX"))
