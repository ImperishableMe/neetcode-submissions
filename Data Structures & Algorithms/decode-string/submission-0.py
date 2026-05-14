class Solution:
    def decodeString(self, s: str) -> str:
        stack: list[tuple[int, str]] = [] # (cnt, enc)
        cnt, cur = 0, ''

        for c in s:
            if c.isdigit():
                cnt = cnt * 10 + int(c)
            elif c == '[':
                stack.append((cnt, cur))
                cnt, cur = 0, ''
            elif c == ']':
                p_cnt, p_cur = stack.pop()
                cur = p_cur + cur * p_cnt
            else:
                cur += c
        return cur
