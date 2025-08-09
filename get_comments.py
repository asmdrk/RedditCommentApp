from joblib import load
import pandas as pd
import praw
import os
# load the saved pipleine model
# TODO: look into hosting stuff
pipeline = load("text_classification.joblib")

cid = os.getenv("CID")
secret = os.getenv("SECRET")
reddit = praw.Reddit(
    client_id=cid,
    client_secret=secret,
    user_agent=os.getenv("USER_AGENT"),
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
    return comments


# take in comments and return predictions
def get_predictions(comments):
    return pipeline.predict(comments)
