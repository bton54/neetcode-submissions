class Solution:
    def ladderLength(self, startWord: str, endWord: str, wordList: List[str]) -> int:
        
        # edge cases
        if len(startWord) != len(endWord):
            return 0

        if startWord == endWord: return 1

        if startWord != endWord and len(wordList) == 0: return 0


        # BFS search

        # we want to take the start word - calculate all combinations of modifying each char in the string
            # add them to the visited set

            # if any words match the endWord - return the # so far
            # if any words match a wordList - add that to the queue and search it

        # convert wordList into a set for fast O(1) lookup
        wordSet = set(wordList)

        if endWord not in wordList:
            return 0


        visited = set()
        visited.add(startWord)

        queue = deque([ ( startWord, 1) ])

        while queue:
            word, transformation_count = queue.popleft()

            # generate all 1-letter variations

            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char == word[i]: # if it's the same letter, skip it
                        continue
                    # replace the character
                    new_word = word[:i] + char + word[i+1:]

                    


                    if new_word == endWord:
                        return transformation_count + 1
                    
                    elif new_word in wordSet:
                        if new_word in visited:
                            continue
                        visited.add(new_word)
                        
                        queue.append((new_word, transformation_count + 1))

        return 0
