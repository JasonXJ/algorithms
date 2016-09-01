from collections import namedtuple

Tweet = namedtuple('Tweet', 'id, time')

class User:
    def __init__(self, userId):
        self.userId = userId
        self.following = set()
        self.tweets = []

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}  # map: id -> `User` object
        self.time = 1


    def getUser(self, userId):
        user = self.users.get(userId)
        if user is None:
            user = self.users[userId] = User(userId)
        return user
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        user = self.getUser(userId)
        user.tweets.append(Tweet(tweetId, self.time))
        self.time += 1
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        user = self.users.get(userId)
        if user is None:
            return []
        candidates = [[user.tweets, len(user.tweets) - 1]]
        for followeeId in user.following:
            followee = self.users.get(followeeId)
            if followee is not None and len(followee.tweets) > 0:
                candidates.append([followee.tweets, len(followee.tweets) - 1])

        rv = []
        while len(rv) != 10:
            selected_candidate = None
            max_tweet_time = float('-inf')
            for candidate in candidates:
                tweets, index = candidate
                if index >= 0 and tweets[index].time > max_tweet_time:
                    max_tweet_time = tweets[index].time
                    selected_candidate = candidate
            if selected_candidate is None:
                break
            rv.append(selected_candidate[0][selected_candidate[1]].id)
            selected_candidate[1] -= 1

        return rv
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        self.getUser(followerId).following.add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        follower = self.users.get(followerId)
        if follower is not None:
            follower.following.discard(followeeId)


if __name__ == "__main__":
    def t1():
        print('=========t1==========')
        twitter = Twitter();

        # User 1 posts a new tweet (id = 5).
        twitter.postTweet(1, 5);

        # User 1's news feed should return a list with 1 tweet id -> [5].
        print(twitter.getNewsFeed(1))

        # // User 1 follows user 2.
        twitter.follow(1, 2);

        # // User 2 posts a new tweet (id = 6).
        twitter.postTweet(2, 6);

        # // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
        # // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
        print(twitter.getNewsFeed(1))

        # // User 1 unfollows user 2.
        twitter.unfollow(1, 2);

        # // User 1's news feed should return a list with 1 tweet id -> [5],
        # // since user 1 is no longer following user 2.
        print(twitter.getNewsFeed(1))
    t1()

    def t2():
        print('=========t2==========')
        twitter = Twitter();

        # User 1 posts a new tweet (id = 5).
        twitter.postTweet(1, 5);

        twitter.postTweet(1, 3);

        # User 1's news feed should return a list with 1 tweet id -> [5].
        print(twitter.getNewsFeed(1))
    t2()

