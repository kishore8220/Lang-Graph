from langchain_ollama.llms import OllamaLLM
from langchain.agents import create_react_agent , AgentExecutor
from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv
from langchain.agents import Tool
from langchain import hub
from datetime import datetime
load_dotenv()

llm = OllamaLLM(model = "qwen3" , temperature=0.3)

def get_today_date():
    """Returns today's date in DD-MM-YYYY format."""
    return datetime.now().strftime("%d-%m-%Y")

tools = [
    TavilySearchResults(search_depth="advanced"),
    Tool(
        name="get_today_date",
        func=get_today_date,
        description="Returns today's date in DD-MM-YYYY format."
    )
]
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt=prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True , handle_parsing_errors=True)
query = executor.invoke({"input": "When was SpaceX's last launch and how many days ago was that from this today?"})
print(query)