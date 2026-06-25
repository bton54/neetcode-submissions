from collections import defaultdict
import heapq
class Twitter:

    # my thought process is to use 3 maps
        # posting map (user -> list of posts)
        # follower map (user -> people who follow us)
        # follwee / following map (user -> people we follow)

    # note, everyone is their own follower
    # also, to show the most "recent" tweet IDs, we can:
        # use a heap to populate the youngest timestamps per tweet. 
        # furthermore, we can store this as a class variable that iterates per tweet.

    # if we publish a new tweet, we can map it instead of the tweet (posting) map
    # this is kinda tricky though, how we want to implement this per user.

    # we can start with the follower map and following map and the follow functions

    def __init__(self):
        # we want to map keys to lists
        # removing from a list is pretty expensive, what if we used a set? 
        self.follower_map = defaultdict(set)
        self.following_map = defaultdict(set)
        self.time = 0

        # thoughts on this solution? 
            # we can store all of the tweets inside of a min-heap sorted by time.

        # when a user fetches for their feed
            # they go through the heap and ask - are we following this person?
                # if so, we can increment the count.
                # return count for 10 posts

        self.tweet_heap = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        # load the tweet onto the map, sorted by tweetId
        heapq.heappush(self.tweet_heap, (-self.time, tweetId, userId))    
        self.time += 1    

    def getNewsFeed(self, userId: int) -> List[int]:
        
        # for this user, we go through the tweet_heap in order
            # for each tweet in the tweet heap we check if we're following this person or not

        count = 0
        tweets = []
        heap_copy = self.tweet_heap.copy()

        while count != 10 and heap_copy:
            time, tweet_id, user_id = heapq.heappop(heap_copy)
            time = -time
            # if we're following this person or its ourself
            if user_id in self.following_map[userId] or userId == user_id:
                tweets.append(tweet_id)

                count += 1

        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        # followerId is now following followeeId
        self.following_map[followerId].add(followeeId)
        # followee has gained a follower - followerId
        self.follower_map[followeeId].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # followerId is no longer following followee
        if followeeId in self.following_map[followerId]:

            self.following_map[followerId].remove(followeeId)
        # followee lost a follower - followerId
        if followerId in self.following_map[followeeId]:
            self.follower_map[followeeId].remove(followerId)