import random

class RandomizedSet:
    def __init__(self):
        self.l, self.d = [], {}

    def insert(self, v):
        if v in self.d: return False
        self.d[v] = len(self.l)
        self.l.append(v)
        return True

    def remove(self, v):
        if v not in self.d: return False
        i, last = self.d[v], self.l[-1]
        self.l[i], self.d[last] = last, i
        self.l.pop()
        del self.d[v]
        return True

    def getRandom(self):
        return random.choice(self.l)