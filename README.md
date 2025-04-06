# LinkedIn-Automation-

Automate your brand-building on LinkedIn — from finding trending content to crafting engaging posts and publishing them, all in one go!

## Overview

This project is a Python-based automation pipeline that:
1. **Searches** for trending articles related to a given topic (e.g., Artificial Intelligence),
2. **Reframes** the content into a professional and engaging LinkedIn-style post, and
3. **Uploads** the post directly to your LinkedIn account.

It's designed for students, professionals, and creators who want to stay consistent on LinkedIn without spending hours creating content.


## Project Structure

├── main.py                 # Main controller script
├── news_browser_to_text.py # Fetches & extracts trending article content
├── refrramer.py            # Reframes raw content into a polished LinkedIn post
├── upload.py               # Uploads post to LinkedIn
├── linksearch.py           # (Optional) Support module for article search
├── linkedinauto.py         # (Optional) Alternate automation script
├── test.py                 # Test script for isolated functions
├── .env                    # Stores environment variables (e.g., LinkedIn API credentials)
├── reframed.txt            # Stores generated LinkedIn post
├── results.txt             # Final posted content log


## How It Works

### 1. `main.py` — Master Script

Run this file to trigger the full pipeline. It:
- Accepts a topic keyword (e.g., `"Artificial Intelligence"`)
- Runs the other 3 scripts sequentially:
  - `news_browser_to_text.py`
  - `refrramer.py`
  - `upload.py`

### 2. `news_browser_to_text.py`

Uses browser automation or scraping logic to:
- Search for trending news articles based on your keyword
- Extract and summarize the main text

### 3. `refrramer.py`

Uses natural language processing (NLP) or prompt-based LLM methods to:
- Reframe the raw content into a student-friendly, professional, and exciting post
- Adds structure, personal voice, and relevant hashtags

### 4. `upload.py`

Posts the content to your LinkedIn profile using:
- LinkedIn API (or)
- Browser automation (e.g., Selenium)

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- `pip` (Python package manager)
- A LinkedIn account
- (Optional) LinkedIn API credentials

### Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure your `.env` file contains your LinkedIn credentials or API token:

```env
LINKEDIN_USERNAME=your_email
LINKEDIN_PASSWORD=your_password
# Or API_KEY=...
```

---

## Usage

```bash
python main.py
```

You'll be prompted to enter a topic (e.g., `Artificial Intelligence`). The pipeline will generate a post and publish it.


## 📄 Example Output

```text
Okay, so I've been nerding out on the future of aerospace lately, and let me tell you, it's seriously next-level! ...

#AerospaceEngineering #FutureOfFlight #Innovation #AI
```

See `reframed.txt` and `results.txt` for generated and posted content samples.


## Why Use This?

- Maintain **consistent** LinkedIn activity
- Save **hours** of writing time
- Stay **ahead of trends**
- Great for **students**, **creators**, and **tech enthusiasts**


## Roadmap / Ideas

- ✅ Automate content search
- ✅ Reframe posts for LinkedIn
- ✅ Auto-post on LinkedIn
- 🔲 Add support for image or video posts
- 🔲 Integrate with ChatGPT API for dynamic rewriting
- 🔲 Schedule posts in advance


## Credits

Developed with 💡 by Arka Bera.


## 📜 License

This project is open-source.
