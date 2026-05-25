"""
Collect public Reddit posts and comments without Reddit API credentials.

This script uses public Reddit JSON endpoints for academic coursework.
It collects posts from selected subreddits and keywords, then retrieves
comment reply relationships for network analysis.

Output:
data/reddit_ai_jobs_public.csv
"""

import time
import random
import requests
import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

OUTPUT_PATH = DATA_DIR / "reddit_ai_jobs_public.csv"

HEADERS = {
    "User-Agent": "SMNA_Assignment2_AI_Job_Anxiety/1.0 academic project"
}

SUBREDDITS = [
    "cscareerquestions",
    "jobs",
    "careerguidance",
    "ArtificialIntelligence",
    "technology",
    "learnprogramming"
]

KEYWORDS = [
    "AI jobs",
    "job replacement",
    "automation",
    "career anxiety",
    "ChatGPT jobs",
    "AI layoffs",
    "reskilling",
    "software engineering jobs",
    "entry level AI",
    "AI replacing programmers"
]

POST_LIMIT_PER_QUERY = 8
COMMENT_LIMIT_PER_POST = 30
SLEEP_SECONDS = 2


def safe_get_json(url, params=None):
    """Safely request JSON from Reddit public endpoint."""
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            params=params,
            timeout=20
        )

        if response.status_code != 200:
            print(f"[WARN] Status {response.status_code} for {url}")
            return None

        return response.json()

    except Exception as e:
        print(f"[ERROR] {e}")
        return None


def clean_text(value):
    if value is None:
        return ""
    return str(value).replace("\n", " ").strip()


def flatten_comments(comment_listing, post_info, rows, parent_author=None):
    """
    Recursively flatten Reddit comments.
    Creates rows with author and parent_author for reply-network construction.
    """
    if not comment_listing:
        return

    children = comment_listing.get("data", {}).get("children", [])

    count = 0
    for child in children:
        if count >= COMMENT_LIMIT_PER_POST:
            break

        if child.get("kind") != "t1":
            continue

        data = child.get("data", {})

        comment_id = data.get("id", "")
        author = data.get("author", "")
        body = clean_text(data.get("body", ""))

        if not body or body in ["[deleted]", "[removed]"]:
            continue

        rows.append({
            "post_id": post_info["post_id"],
            "comment_id": comment_id,
            "subreddit": post_info["subreddit"],
            "created_utc": data.get("created_utc", ""),
            "author": author,
            "parent_author": parent_author,
            "title": post_info["title"],
            "text": body,
            "score": data.get("score", 0),
            "num_comments": post_info["num_comments"],
            "url": post_info["url"],
            "keyword": post_info["keyword"],
            "parent_id": data.get("parent_id", "")
        })

        replies = data.get("replies")
        if isinstance(replies, dict):
            flatten_comments(
                replies,
                post_info,
                rows,
                parent_author=author
            )

        count += 1


def collect_posts_and_comments():
    rows = []
    seen_posts = set()

    for subreddit in SUBREDDITS:
        for keyword in KEYWORDS:
            print(f"\nSearching r/{subreddit} for: {keyword}")

            search_url = f"https://www.reddit.com/r/{subreddit}/search.json"
            params = {
                "q": keyword,
                "restrict_sr": "1",
                "sort": "relevance",
                "t": "year",
                "limit": POST_LIMIT_PER_QUERY
            }

            search_json = safe_get_json(search_url, params=params)
            time.sleep(SLEEP_SECONDS + random.random())

            if not search_json:
                continue

            posts = search_json.get("data", {}).get("children", [])

            for post in posts:
                if post.get("kind") != "t3":
                    continue

                post_data = post.get("data", {})
                post_id = post_data.get("id", "")

                if not post_id or post_id in seen_posts:
                    continue

                seen_posts.add(post_id)

                title = clean_text(post_data.get("title", ""))
                selftext = clean_text(post_data.get("selftext", ""))

                post_info = {
                    "post_id": post_id,
                    "comment_id": "",
                    "subreddit": subreddit,
                    "created_utc": post_data.get("created_utc", ""),
                    "author": post_data.get("author", ""),
                    "parent_author": "",
                    "title": title,
                    "text": f"{title} {selftext}".strip(),
                    "score": post_data.get("score", 0),
                    "num_comments": post_data.get("num_comments", 0),
                    "url": "https://www.reddit.com" + post_data.get("permalink", ""),
                    "keyword": keyword,
                    "parent_id": ""
                }

                # Add post itself as a text record
                if post_info["text"]:
                    rows.append(post_info)

                comments_url = f"https://www.reddit.com/comments/{post_id}.json"
                comments_json = safe_get_json(comments_url)
                time.sleep(SLEEP_SECONDS + random.random())

                if not comments_json or len(comments_json) < 2:
                    continue

                comment_listing = comments_json[1]
                flatten_comments(
                    comment_listing,
                    post_info,
                    rows,
                    parent_author=post_info["author"]
                )

                print(
                    f"Collected post {post_id} | total rows so far: {len(rows)}"
                )

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = collect_posts_and_comments()

    if df.empty:
        print("No data collected. Reddit may have blocked public JSON requests.")
    else:
        df = df.drop_duplicates(subset=["post_id", "comment_id", "text"])
        df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")
        print("\nCollection complete.")
        print("Rows:", len(df))
        print("Saved to:", OUTPUT_PATH)