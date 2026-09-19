class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        if len(s) != len(t):
            return False
        else:
            for letter_s, letter_t in zip(s, t):
                if letter_s not in dict_s:
                    dict_s[letter_s] = 1
                else:
                    dict_s[letter_s] += 1
                    
                if letter_t not in dict_t:
                    dict_t[letter_t] = 1
                else:
                    dict_t[letter_t] += 1
                
        return dict_s == dict_t
            
        