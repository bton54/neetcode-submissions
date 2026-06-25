class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can use a hashmap to quickly look up values
        # we can go through the list of njums and calculate the complement
            # the hashmap lets us quickly see if we have it
            # if so, return the index of the complement
            # if not, add the value into the map
            # the "in" command checks key existance
            # the value is the index

        m_map = {}

        # we need to use enumerate to generate an index as we iterate through this solution
        for i, num in enumerate(nums):
            complement = target - num
            if complement in m_map:
                return [m_map[complement], i] # storing the index as the value here

            else:
                m_map[num] = i

        return -1
