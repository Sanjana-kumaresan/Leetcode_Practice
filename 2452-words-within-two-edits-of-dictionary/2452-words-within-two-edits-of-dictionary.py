class Solution(object):
    def twoEditWords(self, queries, dictionary):
        res = []
        for q in queries:
            for d in dictionary:
                if sum(a != b for a, b in zip(q, d)) <= 2:
                    res.append(q)
                    break
        return res      