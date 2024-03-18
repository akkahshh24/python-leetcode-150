class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create a frequency map for magazine string
        mag_dict = {}

        for ch in magazine:
            if ch not in mag_dict:
                mag_dict[ch] = 1
            else:
                mag_dict[ch] += 1

        # print(mag_dict)

        # iterate through ransom string and decrease the frequency

        for ch in ransomNote:
            if ch not in mag_dict or mag_dict[ch] == 0:
                return False
            else:
                mag_dict[ch] -= 1

        return True