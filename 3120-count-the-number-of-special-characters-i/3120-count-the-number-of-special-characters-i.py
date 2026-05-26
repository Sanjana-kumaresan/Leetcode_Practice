class Solution(object):
    def numberOfSpecialChars(self, word):
        c=0
        set1=set(word)
        for i in range(len(word)):
            if word[i].isupper():
                if word[i].lower() in set1:
                    c+=1
                    set1.remove(word[i].lower())
        return c