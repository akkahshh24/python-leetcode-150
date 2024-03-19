class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 1:
        # defaultdict provides a default value for keys 
        # that haven't been set yet
        anagram_dict = defaultdict(list)

        for s in strs:
            # eat -> aet
            s_sorted = "".join(sorted(s))
            # d[aet] = ['eat', 'tea', 'ate']
            anagram_dict[s_sorted].append(s)
        
        return anagram_dict.values()

        # # Solution 2: 
        # anagram_dict = defaultdict(list)

        # for s in strs:
        #     # 1 0 0 1 ... 0
        #     # a b c d ... z
        #     letterCount = [0] * 26

        #     for l in s:
        #         # calculating the index value and incrementing
        #         letterCount[ord(l) - ord('a')] += 1

        #     key = tuple(letterCount)
        #     anagram_dict[key].append(s)
            
        # return anagram_dict.values()