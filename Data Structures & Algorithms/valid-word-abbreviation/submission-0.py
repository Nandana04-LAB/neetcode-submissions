class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j = 0,0
        while i<len(word) and j<len(abbr):
            if abbr[j].isalpha():
                if abbr[j]!=word[i]:
                    return False
                i=i+1
                j=j+1
            else:
                if abbr[j] == '0':
                    return False
                num=0 # to take particulanumber alone if it is 12 ..it should only take '1'
                while j<len(abbr) and abbr[j].isdigit():
                    num=num*10 + int(abbr[j])
                    j=j+1
                i=i+num
        return i==len(word) and j==len(abbr)