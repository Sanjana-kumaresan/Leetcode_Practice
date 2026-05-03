class Solution(object):
    def rotateString(self, s, goal):
        length = len(s)
        s = list(s)
        goal = list(goal)
        for i in range(length):
            element = s.pop(0)
            s.append(element)

            if s == goal:
                return True
        return False     