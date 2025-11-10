import praw
import pandas as pd
import datetime

class reddit_scraper:
    def __init__(self, client_id, client_secret, user_agent):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent

    def get_reddit(self):
        reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent
        )
        return reddit

    def get_subreddit(self, reddit, subreddit_name):
        subreddit = reddit.subreddit(subreddit_name)
        return subreddit

    def get_popular(self,your_sub):
        reddit = self.get_reddit()
        popular_subs = [sub.display_name.lower() for sub in reddit.subreddits.popular(limit=100000)]
        if your_sub in popular_subs:
            return 'Yes, this is a subreddit.'
        else:
            return 'No, this is not a subreddit.'

    def get_submissions(self, subreddit, limit):
        submissions = []
        for post in subreddit.hot(limit=limit):
            post.comments.replace_more(limit=0)
            for comment in post.comments.list():
                submissions.append({
                    "subreddit": subreddit.title,
                    "post_title": post.title,
                    "comment": comment.body,
                    "score": comment.score,
                    "created_utc": datetime.datetime.fromtimestamp(comment.created_utc),
                    "comment_author": str(comment.author),
                    "permalink": f"https://reddit.com{comment.permalink}"
                })
        return submissions

    def get_data(self, subreddit_name, limit):
        reddit = self.get_reddit()
        subreddit = self.get_subreddit(reddit, subreddit_name)
        submissions = self.get_submissions(subreddit, limit)
        df = pd.DataFrame(submissions)
        df.to_csv(f'{subreddit_name}_comments.csv', index=False)
        return df