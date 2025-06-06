# Lang-Graph
# END to END
A collection of scripts and agents for experimenting with LangChain, Ollama LLMs, and agent-based workflows for content generation, search, and reflection.

## Project Structure

```
.env
scripts/
  ReACT/
    basic.py
    basic1.py
    google-search.py
  reflection-agent/
    chains.py
    graph.py
```

## Setup

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies** (recommended: use a virtual environment):

   ```sh
   pip install langchain langchain_ollama langchain_community langchain_core langgraph python-dotenv
   ```

3. **Set up environment variables**  
   Edit the `.env` file with your API keys (e.g., Tavily, Google):

   ```
   TAVILY_API_KEY=your-tavily-api-key
   GOOGLE_CSE_ID=your-google-cse-id
   GOOGLE_API_KEY=your-google-api-key
   ```

## Scripts Overview

### `scripts/ReACT/basic.py`

- Uses Ollama LLM and Tavily search to answer questions, with a tool for today's date.
- Example usage:  
  ```sh
  python scripts/ReACT/basic.py
  ```

### `scripts/ReACT/basic1.py`

- Similar to `basic.py` but uses a different agent setup and date format.
- Example usage:  
  ```sh
  python scripts/ReACT/basic1.py
  ```

### `scripts/ReACT/google-search.py`

- Demonstrates Google Search API integration via LangChain tools.
- Example usage:  
  ```sh
  python scripts/ReACT/google-search.py
  ```

### `scripts/reflection-agent/chains.py`

- Defines prompt templates and chains for tweet generation and reflection using Ollama LLM.

### `scripts/reflection-agent/graph.py`

- Builds a LangGraph workflow for iterative tweet generation and critique.
- Example usage:  
  ```sh
  python scripts/reflection-agent/graph.py
  ```

## Notes

- Requires [Ollama](https://ollama.com/) running locally for LLM inference.
- Make sure your API keys are valid and have sufficient quota.
- The project is intended for experimentation and educational purposes.

## License

MIT License
