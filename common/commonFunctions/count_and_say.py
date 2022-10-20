from __future__ import annotations


class CountAndSay(tuple[int, str]):
    @staticmethod
    def say(n: int):
        s = "1"
        for itr in range(1, n):
            snew, pr = "", 0
            for i in range(1,len(s)):
                if s[i] != s[i-1]:
                    snew += str(i-pr) + s[pr]
                    pr = i
            s = snew + str(len(s)-pr) + s[pr]
        return s
