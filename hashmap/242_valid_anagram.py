class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1:
        # s_sorted = ''.join(sorted(s))
        # t_sorted = ''.join(sorted(t))
        # return s_sorted == t_sorted

        # Solution 2:
        # return sorted(s) == sorted(t)

        # Solution 3:
        # return Counter(s) == Counter(t)

        # Solution 4:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for ch1, ch2 in zip(s, t):
            countS[ch1] = 1 + countS.get(ch1, 0)
            countT[ch2] = 1 + countT.get(ch2, 0)

        for k, v in countS.items():
            if v != countT.get(k, 0):
                return False

        return True