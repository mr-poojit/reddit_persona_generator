import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="reddit-persona-bot"
)

def scrape_user_data(username, limit=100):
    user = reddit.redditor(username)
    data = []

    for comment in user.comments.new(limit=limit):
        data.append({
            "type": "comment",
            "text": comment.body,
            "url": f"https://reddit.com{comment.permalink}"
        })

    for submission in user.submissions.new(limit=limit):
        text = f"{submission.title}\n\n{submission.selftext}" if submission.is_self else submission.title
        data.append({
            "type": "post",
            "text": text,
            "url": f"https://reddit.com{submission.permalink}"
        })

    return data
