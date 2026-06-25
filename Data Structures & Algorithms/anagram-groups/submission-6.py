class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can efficiently group the anagrams into sublists sorting each word
            # if words are the same when sorted they are anagrams
            # we can map them into a hash map using the sorted word as the key and the value as a list of the words

        # this is somewhat inefficient though, where m * n log n is the TC
            # m = the number of words
            # n is the number of characters in the longest word

        # this also uses O(n) space for the map

        # hmm ... 

        hashmap = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            # there's no built in s.sort()
            # instead - join an empty list with the sorted(s)  

            hashmap[sorted_s].append(s)

        # now we need to return a list of the sublists? 
        # return hashmap.values()
            # wrong syntax - we can build a res
        
        res = []


        for sublist in hashmap.values():
            res.append(sublist)

        return res
