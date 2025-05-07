import praw
import pandas as pd

# Step 1: Load the extracted keywords CSV
df_keywords = pd.read_csv('extracted_keywords.xls')

# Step 2: Extract top keywords for each document
# Get the top 3 keywords (or adjust the number as needed) for each row
top_keywords_per_row = df_keywords.apply(lambda row: row[row > 0].nlargest(10).index.tolist(), axis=1)

# Flatten the list of lists into a single list
dynamic_keywords = [keyword for keywords in top_keywords_per_row for keyword in keywords]

# Step 3: Combine with static keywords
static_keywords = ["innovation", "AI", "machine learning", "blockchain", "cloud", "agile"]
combined_keywords = list(set(static_keywords + dynamic_keywords))  # Deduplicate

# Step 4: Print or save the combined keywords
print(f"Total combined keywords: {len(combined_keywords)}")
print("Sample keywords:", combined_keywords[:10])

# Save combined keywords to a file (optional)
pd.DataFrame({'Keywords': combined_keywords}).to_csv('combined_keywords.csv', index=False)
print("Combined keywords saved to 'combined_keywords.csv'")

# Define subreddits and keywords 
subreddits = ["technology", "technews", "Futurology", "startups"]
keywords = ["innovation", "AI", "machine learning", "blockchain", "cloud", "agile"]
# Load combined keywords
combined_keywords = pd.read_csv('combined_keywords.csv')['Keywords'].tolist()

# Reddit API
reddit = praw.Reddit(
    client_id='Ix76zFnrRCMqMq7U52PYGQ',
    client_secret='5lsOi-uw5yFDViwR706ITq8wTnn2gQ',
    user_agent='reditstream',
    username='Solid-Theory-5148',
    password='56111051729AS'
)
def fetch_reddit_posts(subreddits, keywords, limit=250):
    data = []
    for subreddit in subreddits:
        print(f"Fetching posts from r/{subreddit}...")
        for post in reddit.subreddit(subreddit).new(limit=limit):
            # Filter posts by keywords
            if any(keyword.lower() in post.title.lower() or 
                   (post.selftext and keyword.lower() in post.selftext.lower()) 
                   for keyword in keywords):
                # Fetch top-level comments
                comments = []
                post.comments.replace_more(limit=0)  # Fetch only top-level comments
                for comment in post.comments:
                    comments.append(comment.body)
                
                data.append({
                    "Title": post.title,
                    "Content": post.selftext if post.selftext else "No Content",
                    "Upvotes": post.score,
                    "Comments_Count": post.num_comments,
                    "Top_Comments": comments[:10],
                    "Created": pd.to_datetime(post.created_utc, unit="s"),
                    "Author": post.author.name if post.author else "Unknown",
                    "URL": post.url
                })
    return pd.DataFrame(data)

# display data
# Use combined keywords in the fetch_reddit_posts function
reddit_data = fetch_reddit_posts(subreddits, combined_keywords)
print(f"Fetched {len(reddit_data)} relevant posts.")

reddit_data.to_csv("reddit_raw_data.csv", index=False)
print("Data saved : 'reddit_raw_data.csv'")