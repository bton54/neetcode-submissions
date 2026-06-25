class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # there's a few ways to check if strings are anagrams
            # same frequencies of characters
                # we iterate through both words and track + compare frequencies
                    # we go through the first and use them to iterate +1
                    # then the second - -1
                    # if any values != 0 then we have diff 

            # same word when sorted
                # sort each word + compare
                # 2 * n log n is more expensive

        # frequency method is more efficient time wise

        s_map = defaultdict(int) # empty list -> integer, default 0

        for c in s:
            s_map[c] += 1

        # then we want to subtract that value 
        for c in t:
            s_map[c] -= 1

        # then we iterate through the values and if there's a non zero, return False

        # otherwise return true

        for freq in s_map.values():
            if freq != 0:
                return False

        return True

        