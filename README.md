# 🦊 Reddit Scraper

[reddit](<img width="1168" height="593" alt="image" src="https://github.com/user-attachments/assets/194177db-18d2-4970-9f81-2b97919e352d" />

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
