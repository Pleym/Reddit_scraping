import praw
from config import PRAW_SECRET, PRAW_USER_CLIENT, PRAW_KEY
import pandas as pd 
from datetime import datetime

"""
Login to Reddit
"""
reddit = praw.Reddit(
    client_id=PRAW_USER_CLIENT,
    client_secret=PRAW_SECRET,
    password=PRAW_KEY,
    username="Pleymoubile",
    user_agent="Reedit_user",
)
"""
try to scrap the hot posts in subreddit
"""
subreddit_op = reddit.subreddit("Frugal").top('all',limit=1000)
subreddit_cons = reddit.subreddit("ConsumerReports").top('all',limit=1000)
df_topics = []
df_comments = []
df_2_topics= []
df_2_comments = []
for submission in subreddit_cons:
    date = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')
    df_topics.append([submission.title, submission.id,date, submission.num_comments,submission.score,submission.selftext])
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        df_comments.append([submission.title, submission.id,comment.id, comment.parent_id, datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'), comment.score, comment.body])

df_topics = pd.DataFrame(df_topics,columns=["title", "id","date","num_comments","score","context"])
df_comments = pd.DataFrame(df_comments, columns= ["title","message_id","comment_id","parent_id","date","score","message"])
for _ in subreddit_op:
    date = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')
    df_2_topics.append([_.title, _.id, date,_.num_comments,_.score,_.selftext])
    for comment in submission.comments.list():
        df_2_comments.append([submission.title, submission.id,comment.id, comment.parent_id, datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'), comment.score, comment.body])

df_2_topics = pd.DataFrame(df_2_topics,columns=["title", "id","date","num_comments","score","context"])
df_2_comments = pd.DataFrame(df_2_comments, columns= ["title","message_id","comment_id","parent_id","date","score","message"])


result_comments = pd.concat([df_comments,df_2_comments])
result_topics = pd.concat([df_topics,df_2_topics])
result_comments.to_csv("top_comments_frugal_ConsumerReports.csv",index=False)
result_topics.to_csv("top_topics_frugal_ConsumerReports.csv",index=False)