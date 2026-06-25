class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we know the sorting appraoch but that sucks cuz that's n number of n log n sorts
        # the hashmap approach requires us to know the ord(c) - ord('a') syntax
        # tldr we need to know the counts of all the characters per string
        # then we want to store that in a count array, tuplize it, and then add it to the result map

        # we use the tuple of counts as the key, and string as teh value

        res = defaultdict(list)
        for s in strs:
            # define a count map for each of the 26 letters in the alphabet
            count = [0] * 26

            # iterate through the characters in the string
            for char in s:
                # get the value
                value = ord(char) - ord('a') # this converts ur character to a num between 1-26
                count[value] += 1

            # now use this count as a key and map it to the string
            res[tuple(count)].append(s)

        return list(res.values())