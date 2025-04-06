from google import genai
from google.genai import types

api_key = "AIzaSyAG0o2KrxbXbsdqeyZ5rz9NpWDIRTk8Rtc"

# Assign name and character directly
llm_name = "Aariz"

llm = genai.Client(api_key=api_key)

filepath = "//Users/arkabera/Desktop/VS code/Automate LinkedIn/results.txt"

with open(filepath, "r", encoding="utf-8") as file:
    contents = file.read()  # Read entire file content
    # print(contents)


# System instruction for Aariz
sys_instruct = f"""
You are a Blog Writer. This is the content and a little brief detail about what you have to write about : {contents}.
write a short about 300 words for a blog, it is to tell about what i understand about the topic, and have to give a opinion about the same
write it in te manner that you are the one telling about some of your research, i want your tone to be professional
also in the end give me the appropriate hashtags that suit the content
"""

user_input = "write a blog for an post about the given topic, keep the tone to be cool tecnical and like a student"

llm_response = llm.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction=sys_instruct),
    contents=[user_input]
)
    

print(llm_response.text)

re_path = "/Users/arkabera/Desktop/VS code/Automate LinkedIn/newsfetch/reframed.txt"

with open(re_path, "w") as file:
    pass

with open(re_path, "a") as file:
    file.write(f"{llm_response.text}")