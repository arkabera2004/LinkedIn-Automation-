import logging
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set logging level to WARNING to suppress INFO messages
logging.basicConfig(level=logging.WARNING)

# Initialize the model
api_key = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=SecretStr(api_key))

filepath = "/Users/arkabera/Desktop/VS code/Automate LinkedIn/newsfetch/reframed.txt"

with open(filepath, "r", encoding="utf-8") as file:
    contents = file.read()  # Read entire file content


async def main():
    
    # Ask the user what they want to search

    credentials = "email : arkabera2004@gmail.com password: rimabera"  
    
    permission = (f"{credentials} I give you complete authority to use my credentials for the purpose when necessary. Create a new linked in post saying {contents} . ")
    
    user_query = permission 

    
    
    # Initialize the AI agent with the user input
    agent = Agent(
        task=user_query,  # Use user input as the task
        llm=llm,
    )
    
    # Run the agent and get results
    result = await agent.run()
    
    # Extract and print only the relevant response (fixes the unwanted output issue)
    if hasattr(result, "extracted_content") and isinstance(result.extracted_content, str):
        print("\n🔍 Search Result:")
        print(result.extracted_content)
    else:
        print("\n❌ No relevant content found.")

# Run the async function
asyncio.run(main())
