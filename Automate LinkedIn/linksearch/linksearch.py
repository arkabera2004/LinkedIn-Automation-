import feedparser

# List of RSS feeds from popular tech websites
RSS_FEEDS = {
    "TechCrunch": "https://techcrunch.com/feed/",
    "The Verge": "https://www.theverge.com/rss/index.xml",
    "Wired": "https://www.wired.com/feed/rss",
    "Ars Technica": "https://feeds.arstechnica.com/arstechnica/index",
    "Hacker News": "https://news.ycombinator.com/rss",
}

def fetch_tech_news():
    print("\n===== Latest Tech News =====\n")
    
    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        print(f"\n--- {source} ---\n")
        
        for entry in feed.entries[:5]:  # Fetch top 5 news articles
            print(f"• {entry.title}\n  {entry.link}\n")
    
if __name__ == "__main__":
    fetch_tech_news()
