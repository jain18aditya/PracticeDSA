"""
Problem Statement: Identify Spammers from Activity Logs

You are part of the Spam Prevention Team for a microblogging platform (similar to Twitter/X). Your goal is to detect users who exhibit spam-like behavior based on their activity patterns.

The platform generates an activity log file that records user actions such as posting tweets and retweeting existing tweets.

📂 Input

You are given the absolute path to a log file containing user activity records.

Each log entry represents either:

An original tweet
A retweet of an existing tweet

The exact format of each log line is described in a separate file (log_structure.txt). Each record contains at least:

Timestamp (in milliseconds)
Username
Action type (tweet or retweet)
Tweet ID
(For retweets) Original Tweet ID
🚨 Definition of a Spammer

A user is considered a spammer if they satisfy all of the following conditions:

❌ The user has no original tweets
✅ The user has made at least one retweet
⏱ All retweets made by the user occur within 1000 milliseconds (1 second) of the corresponding original tweet
🧾 Task

Implement the function:

def identify_spammers(logfile_path: str) -> List[str]:

This function should:

Read and process the activity log file
Identify all users who meet the spammer criteria
Return a list of usernames classified as spammers
📤 Output

Return a list of usernames (strings), for example:

["pkoch", "MagnusCarlsen", "user123"]
⚙️ Constraints & Expectations
The log file can be very large (millions or billions of entries)
Your solution should be efficient in time and space
Aim for a solution with O(N) time complexity
Avoid loading unnecessary data into memory
🧪 Example (Conceptual)
1000,userA,tweet,t1
1500,userB,retweet,t2,t1
1800,userB,retweet,t3,t1
userA → has original tweet → NOT spammer
userB → only retweets
All retweets within 1000ms → ✅ spammer
"""
from collections import defaultdict
from typing import List


def identify_spammers(logfile_path: str) -> List[str]:
    original_tweet = {}
    # tweet_id -> timestamp

    user_retweet = defaultdict(list)
    # user -> list of (tweet_id, retweet_timestamp)

    user_original_count = defaultdict(int)

    with open(logfile_path) as f:
        for line in f:
            parts = line.strip().split(",")
            timestamp = parts[0]
            username = parts[1]
            action_type = parts[2]
            tweet_id = parts[3]

            if action_type == "tweet":
                original_tweet[tweet_id] = timestamp
                user_original_count[username] += 1
            elif action_type == "retweet":
                original_tweet_id = parts[4]
                user_retweet[username].append((original_tweet_id, timestamp))

    spammers = []
    for user in user_retweet:
        if user_original_count[user] > 0:
            continue
        if not user_retweet[user]:
            continue
        is_spammer = True
        for tweet_id, retweet_time in user_retweet[user]:
            if tweet_id not in original_tweet:
                is_spammer = False
                break

            original_time = original_tweet[tweet_id]
            if abs(int(original_time) - int(retweet_time)) > 1000:
                is_spammer = False
                break
        if is_spammer:
            spammers.append(user)

    return spammers

print(identify_spammers("spammer.txt"))