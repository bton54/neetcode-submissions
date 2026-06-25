class Solution:
    def minWindow(self, s: str, t: str) -> str:
            # edge cases:
        if len(t) > len(s):
            return ""

        # create the counter map for t

        t_counter = defaultdict(int)

        for char in t:
            t_counter[char] += 1

        s_counter = defaultdict(int) # now we create an empty one
        # once t and s counters match up (or s has all the ones in t, we return true)

        required = len(t_counter) # num of unique chars we need to satisfy
        formed = 0 # how many we have

        # begin sliding window
        min_len = float('inf')
        min_window = ""
        l = 0
        for r in range(len(s)):
            char = s[r]
            s_counter[char] += 1

            # check if this character's frequency matches our requirement
                # if it's one of the characters we need
                # and the count in the s_counter matches the required count
            if char in t_counter and s_counter[char] == t_counter[char]:
                formed += 1 # we've formed 1


            # try to shrink the window from the left if we have a valid window

            while l <= r and formed == required:

                # get the length of the window
                window_len = r-l+1

                # if there's a new valid window that's smaller than the existing
                if window_len < min_len:
                    min_len = window_len
                    min_window = s[l:r+1]

                # remove the left character in the window from the s counter
                left_char = s[l]
                s_counter[left_char] -= 1

                # check if we took out a required character
                    # if that left character was one of the required ones
                    # and now we have less of that character in the s counter than the t counter
                    # AKA if don't have enough
                if left_char in t_counter and s_counter[left_char] < t_counter[left_char]:
                    formed -= 1

                    # reduce the count of the formed chars we have by 1

                l += 1 # shift the left window pointer

        return min_window if min_len != float('inf') else "" 