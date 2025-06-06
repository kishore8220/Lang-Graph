import os

os.environ["GOOGLE_CSE_ID"] = "b0bdc34c178a4451d"
os.environ["GOOGLE_API_KEY"] = "AIzaSyDV9wqt7P-JS8GI0mNCFne8BReLeUefuMU"

from langchain_core.tools import Tool
from langchain_google_community import GoogleSearchAPIWrapper

search = GoogleSearchAPIWrapper()

tool = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=search.run,
)

print(tool.run("top 10 vulnerabilties in 2025?"))