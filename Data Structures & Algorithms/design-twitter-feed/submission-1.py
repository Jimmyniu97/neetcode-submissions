from collections import defaultdict
class Twitter:

    def __init__(self):
        self.follower = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets[userId].append([-self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        userIDs  = self.follower[userId]
        userIDs.add(userId)

        for user in userIDs:
            for tweet in self.tweets[user]:
                heapq.heappush(heap, tweet)
        
        res = []
        while heap and len(res) < 10:
            tweet = heapq.heappop(heap)
            res.append(tweet[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)