class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0] * len(temperatures) # 0 by default

        
        for i in range(len(temperatures)):
            # if we have an element on the top of the stack AND we see a value greater than it
            # update it with the index
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)

        return res
