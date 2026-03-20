import requests
import pandas as pd

HEADERS = {
    "User-Agent": "Sentrix/1.0 by Aarthi"
}

def fetch_reddit_posts(topic, limit=50):
    url = f"https://www.reddit.com/search.json?q={topic}&limit={limit}&sort=new"
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        data = response.json()
        posts = data["data"]["children"]

        results = []
        for post in posts:
            post_data = post["data"]
            title = post_data.get("title", "")
            body  = post_data.get("selftext", "")
            full_text = f"{title}. {body}".strip()

            if len(full_text) > 10:
                results.append({
                    "title": title,
                    "text":  full_text,
                    "score": post_data.get("score", 0),
                    "url":   f"https://reddit.com{post_data.get('permalink', '')}"
                })

        return pd.DataFrame(results)

    except Exception as e:
        print(f"Error fetching Reddit data: {e}")
        return pd.DataFrame()