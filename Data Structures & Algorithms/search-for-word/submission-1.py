class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # recursively explore the 2d grid

        path = set()

        # track coordinate you're exploring + char of the word you need
        def backtracking(i, j, k):
            # base case - did we find the loot?
            if k == len(word):
                return True

            # make sure we're in bounds
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            # if we see the same cell, which we track with the set, return false.
            if (i,j) in path:
                return False

            # we have to make sure this new character matches the character we're looking for

            # the curr char of the board matches the letter in the word we're searching for
            if board[i][j] != word[k]:
                return False

            # now, we know this advances the word
            path.add((i,j))

            # recursively explore in all directions
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            for dx, dy in directions:
                # can we advance the word?
                nx, ny = i + dx, j + dy
                if backtracking(nx, ny, k+1):
                    return True

            path.remove((i,j))
            return False
            

        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if backtracking(i,j,0):
                    return True

        return False
        
        # TC: O(m*n)
        # SC: O(r) , height of the recursion stack

        

            




