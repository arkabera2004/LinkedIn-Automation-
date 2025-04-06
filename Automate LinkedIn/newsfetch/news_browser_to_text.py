import logging
import asyncio
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent

# Load environment variables
load_dotenv()

# Fetch API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Ensure API key is present
if not api_key:
    raise ValueError("GEMINI_API_KEY.env file.")

# Set logging level to WARNING to suppress unnecessary logs
logging.basicConfig(level=logging.WARNING)

# Initialize the LLM model with the API key
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=api_key)

async def fetch_news():
    """ Fetch AI tech news from multiple sources """
    base_query = "visit the first site that comes up and give me the detailed update on the new tech in the domain of  "

    # Ask the user for a specific AI domain
    # user_domain = input("\nEnter a specific AI domain (or press Enter to skip): ").strip()

    user_domain = "aerospace"
    search_query = base_query + user_domain if user_domain else base_query

    print(f"\n🔍 Searching for: {search_query}...\n")

    # Initialize the AI agent
    agent = Agent(task=search_query, llm=llm)
    
    # Run the agent and get results
    result = await agent.run()

async def main():
    top_news = await fetch_news()



# Run the async function
asyncio.run(main())







