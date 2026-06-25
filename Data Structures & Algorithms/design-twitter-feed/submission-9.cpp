class Twitter {
public:
    Twitter() {
        // we can use a map to map a person's following
        // use another unordered_map to map a person's followers
        // use a heap to retrieve the most recent tweets based on time stamp
        // each person has an ID. 

        // we should also have a map where id -> list of tweets (tweet has time stamp) 

        // universal time clock variable

        // but we need to efficiently fetch the news feed of a person
            // iterating and yanking all of the posts for a person's following + there's is od
    }

    int time = 0;
    unordered_map<int, unordered_set<int>> following_map;
    unordered_map<int, unordered_set<int>> follower_map;

    unordered_map<int, vector<pair<int, int>>> tweet_map;
    
    void postTweet(int userId, int tweetId) {
        tweet_map[userId].push_back({tweetId, time});
        time++; 
    }
    
    vector<int> getNewsFeed(int userId) {
        // we need to get the tweets from all of the people that we follow

        // iterate through all the people we follow, load their tweets into a heap indexed by time stamp

        // stores a max heap of pairs of timestamp + tweetId that we can return the top 10 of. 
        priority_queue<pair<int, int>,vector<pair<int,int>>,greater<pair<int,int>>> pq; // min heap

        // now we want to iterate through all of the people we follow, add all of their tweet pairs indexed by time

        for (auto& id : following_map[userId]) {

            if (id == userId) { continue; }
            // we add all of these people's fking tweets into the priority queue indexed by time



            for (auto& [tweetId, time] : tweet_map[id]) {
                pq.push({time, tweetId});

                if (pq.size() > 10) {
                    pq.pop();
                }
            }
        }

        // now we have to add our own tweets

        for (auto& [tweetId, time] : tweet_map[userId]) {
            pq.push({time, tweetId});

            if (pq.size() > 10) {
                pq.pop();
            }
        }

        // now we just return the tweet ids from the heap

        vector<int> res;

        while (!pq.empty()) {
            auto& top = pq.top().second;
            res.push_back(top);
            pq.pop();

        }
        reverse(res.begin(), res.end());
        return res;
    }
    
    void follow(int followerId, int followeeId) {
        follower_map[followeeId].insert(followerId);
        following_map[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        follower_map[followeeId].erase(followerId);
        following_map[followerId].erase(followeeId);
    }
};
