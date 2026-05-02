class Twitter:

    def __init__(self):
        self.ts = 0
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.ts += 1
        self.tweets[userId].append((self.ts, userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followees[userId].add(userId)
        followeePosts = [tweet 
            for uid in self.followees[userId]
            for tweet in self.tweets[uid]
        ]
        followeePosts.sort(key= lambda x: x[0], reverse=True)
        return [tweet[2] for tweet in followeePosts][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if followeeId in self.followees[followerId]:
        self.followees[followerId].discard(followeeId)
