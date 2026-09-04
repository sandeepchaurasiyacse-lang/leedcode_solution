class Solution(object):
    def decodeString(self, s):
        stack = []
        number = 0
        current = ""
        for i in range(len(s)):
            if s[i].isdigit():
                number = number * 10 + int(s[i])
            elif s[i] == "[":
                stack.append((current, number))
                current = ""
                number = 0
            elif s[i] == "]":
                old_string, repeat = stack.pop()
                current = old_string + current * repeat
            else:
                current += s[i]
        return current