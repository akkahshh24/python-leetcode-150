class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1:
        # # lookup_dict contains the number required to reach the target as key
        # # and the index of the current number as value
        # # For example, 
        #     # for number = 2, target = 9,
        #     # key = 7, value = 0
        # lookup_dict = {}

        # # getting the index and element
        # for i, n in enumerate(nums):
        #     if n in lookup_dict:
        #         return [lookup_dict[n], i]
        #     else:
        #         lookup_dict[target - n] = i

        # return None

        # Solution 2:
        lookup_dict = {}

        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in lookup_dict:
                return [lookup_dict[compliment], i]
            else:
                lookup_dict[n] = i

        return None