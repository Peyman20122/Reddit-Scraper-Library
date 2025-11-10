# 🦊 Reddit Scraper

[https://ichef.bbci.co.uk/news/1024/cpsprodpb/13EB4/production/_132888518_gettyimages-2028785635.jpg.webp ](https://pentagram-production.imgix.net/506cc7b9-5998-4798-9420-3be03c1202e7/Reddit_Thumbnail.jpg?auto=compress%2Cformat&crop=entropy&fit=crop&fm=jpg&h=470&q=80&rect=4%2C0%2C2992%2C1870&w=900)

A lightweight Python library for scraping Reddit posts and comments using the [PRAW](https://praw.readthedocs.io/) API.  
This library helps you easily extract data from subreddits, posts, and comments into structured formats like pandas DataFrames or CSV files.

---

## 📦 Features

- Fetch hot, new, or top posts from any subreddit  
- Extract post titles, comments, authors, scores, timestamps, and links  
- Save the results as a CSV file  
- Simple object-oriented interface  
- Built on top of the official Reddit API via **PRAW**

---

## ⚙️ Installation

```bash
pip install praw pandas
```

## 🧩 Class Overview

| Method                              | Description                                      |
| ----------------------------------- | ------------------------------------------------ |
| `get_reddit()`                      | Returns a PRAW Reddit instance                   |
| `get_subreddit(name)`               | Returns a subreddit object                       |
| `get_submissions(subreddit, limit)` | Retrieves posts and comments from a subreddit    |
| `get_data(subreddit_name, limit)`   | Creates a DataFrame and saves the results to CSV |

## 🧰 Requirements

- Python 3.8+
- PRAW
- pandas

## 📜 License

This project is licensed under the MIT License — see the LICENSE
 file for details.
