class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for i in range (len(asteroids)):
            current = asteroids[i]
            while len(stack) > 0 and stack[-1] >0 and current < 0:
                if stack[-1] < abs(current):
                    stack.pop()
                elif stack[-1] == abs(current):
                    stack.pop()
                    current = 0
                    break
                else:
                    current = 0
                    break
            if current != 0:
                stack.append(current)
        return stack
        