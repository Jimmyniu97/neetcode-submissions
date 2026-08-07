from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pattern = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern[word[0:i]+'*'+word[i+1:]].append(word)
        
        queue = deque([(beginWord, 1)])
        visit = set(beginWord)

        while queue:
            curr, count = queue.popleft()
            if curr == endWord:
                return count
            interWords = [curr[0:i]+'*'+curr[i+1:] for i in range(len(curr))]
            for interWord in interWords:
                for w in pattern[interWord]:
                    if w not in visit:
                        visit.add(w)
                        queue.append((w, count+1))
        
        return 0


        


