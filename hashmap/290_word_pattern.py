class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        def helper(word):
            output, lookup = [], {}
            i = 1

            for w in word:
                if w not in lookup:
                    lookup[w] = i
                    i += 1
                output.append(lookup[w])
            
            return output

        return helper(pattern)==helper(words)