import time
import requests

# LinkedIn API Credentials
ACCESS_TOKEN = "your_access_token_here"

def post_to_linkedin(message):
    """Function to post a message on LinkedIn"""
    api_url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    payload = {
        "author": "urn:li:person:your_linkedin_id",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": message},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 201:
        print("Successfully posted on LinkedIn!")
    else:
        print("Error:", response.text)

def automated_greeting():
    """Prints greeting and posts on LinkedIn"""
    print("Hi, how are you?")
    time.sleep(2)
    
    message = "Hello everyone! Hope you're having a great day. #automation #linkedin"
    post_to_linkedin(message)

# Run the function
automated_greeting()
