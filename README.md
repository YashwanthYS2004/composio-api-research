# Composio API Research Agent

Composio is an autonomous research pipeline that analyzes API capabilities, authentication methods, and buildability verdicts for 100 SaaS applications.

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd composio-assignment
```

2. Install dependencies:

```bash
pip install langchain langchain-openai langchain-community tavily-python firecrawl-py
```

3. Set API keys in your environment (examples):

Bash:
```bash
export OPENAI_API_KEY="sk-..."
export TAVILY_API_KEY="tvly-..."
```

PowerShell:
```powershell
$env:OPENAI_API_KEY="sk-..."
$env:TAVILY_API_KEY="tvly-..."
```

## Usage

Run the agent to process the list of 100 apps:

```bash
python agent.py
```

Output: the agent will write `results.json` containing the structured data.

## Verification Approach

To ensure accuracy the pipeline uses a two-pass approach:

- **Extraction:** GPT-4o extracts structured data from search results.
- **Verification:** A secondary prompt asks the LLM to verify whether the provided `evidence_url` supports the extracted `auth_method` and `api_surface`. Entries that fail verification are flagged for human review or re-search.

## Deliverable

Open [index.html](index.html) in any browser to view an interactive 2-minute case study summarizing:

- Patterns discovered across the apps
- The agent architecture
- The final verified matrix for the 100 apps

## Files

- [agent.py](agent.py) — main research agent
- [results.json](results.json) — agent output
- [index.html](index.html) — interactive case study

## Notes

- Run inside a virtual environment and ensure API keys are set before executing the agent.
