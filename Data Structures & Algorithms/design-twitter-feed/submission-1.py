class Twitter:
    def __init__(self):
        self.following = defaultdict(set)      # userId -> set of followeeIds
        self.tweets = defaultdict(list)         # userId -> list of (timestamp, tweetId)
        self.timestamp = 0                      # global monotonic counter

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        # candidates = the user themself + everyone they follow
        candidates = self.following[userId] | {userId}

        # seed the heap with each candidate's most recent tweet
        for uid in candidates:
            tweets = self.tweets[uid]
            if tweets:
                idx = len(tweets) - 1
                ts, tweetId = tweets[idx]
                # max-heap via negated timestamp
                heapq.heappush(heap, (-ts, tweetId, uid, idx))

        result = []
        while heap and len(result) < 10:
            negTs, tweetId, uid, idx = heapq.heappop(heap)
            result.append(tweetId)

            # push the next-older tweet from the same user, if any
            if idx > 0:
                idx -= 1
                ts, nextTweetId = self.tweets[uid][idx]
                heapq.heappush(heap, (-ts, nextTweetId, uid, idx))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
