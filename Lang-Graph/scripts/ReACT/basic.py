from langchain_ollama.llms import OllamaLLM
from langchain.agents import initialize_agent, Tool
from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Initialize LLM
llm = OllamaLLM(model="qwen3")

def get_today_date(_: str) -> str:
    from datetime import datetime
    return datetime.today().strftime("%Y-%m-%d")


today_tool = Tool(
    name="GetTodayDate",
    func=get_today_date,
    description="Returns the current date (today) in YYYY-MM-DD format. Use this instead of a search if you need today's date."
)



# Web search tool (ensure API key is set correctly)
search_tool = TavilySearchResults(search_depth="basic")

# Tools available to the agent
tools = [today_tool,search_tool]

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True
)

# 🧠 Let the agent decide how to solve it
query = "When was SpaceX's last launch and how many days ago was it from today (you can use tools if needed)?"
response = agent.invoke(query)

print(response)
