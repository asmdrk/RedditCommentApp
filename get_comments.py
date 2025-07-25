from joblib import load
import pandas as pd
import praw
import env
# load the saved pipleine model
# TODO: look into hosting stuff
pipeline = load("text_classification.joblib")

cid = "fzvmD-u5jrC3Vh0jee27ig"
secret = env.REDDIT_SECRET

reddit = praw.Reddit(
    client_id=cid,
    client_secret=secret,
    user_agent="python:hatespeech (by /u/326-away)",
    check_for_async=False
)


def get_subreddit_comments(text_query):
    subreddit = reddit.subreddit(text_query)
    comments = []
    count = 0
    for comment in subreddit.stream.comments():
        comments.append(comment.body)
        count += 1
        # If you've processed 20 comments, break out of the loop
        if count >= 20:
            break
    return pipeline.predict(comments)
