class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        cache = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                cache[pattern].append(word)
        
        queue = collections.deque([beginWord])
        visited = {beginWord}
        res = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i]+'*'+word[i+1:]
                    for nei in cache[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            res += 1

        return 0             