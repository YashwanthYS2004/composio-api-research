# agent.py
import os
import json

from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_agent


# --------------------------------------------------
# API keys
# --------------------------------------------------
# Set these in PowerShell instead of hard-coding them:
#
# $env:OPENAI_API_KEY="your-new-openai-key"
# $env:TAVILY_API_KEY="your-new-tavily-key"
#
# Do NOT put the actual keys in this file.


# --------------------------------------------------
# LLM
# --------------------------------------------------
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)


# --------------------------------------------------
# Search tool
# --------------------------------------------------
search = TavilySearchResults(
    max_results=5
)

tools = [search]


# --------------------------------------------------
# Agent
# --------------------------------------------------
system_prompt = """
You are an AI Product Ops expert.

Research the API and integration capabilities of the provided app.

Use search tools to find official documentation whenever possible.

Return a strict JSON object with exactly these keys:

category,
description,
auth_method,
access,
api_surface,
mcp_server,
verdict,
evidence,
human_needed
"""


agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt,
)


# --------------------------------------------------
# Apps to research
# --------------------------------------------------
apps = [
    {
        "name": "Salesforce",
        "hint": "salesforce.com"
    },
    {
        "name": "HubSpot",
        "hint": "hubspot.com"
    }
]


# --------------------------------------------------
# Run agent
# --------------------------------------------------
results = []

for app in apps:
    try:
        query = (
            f"App: {app['name']}, "
            f"Hint: {app['hint']}"
        )

        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            }
        )

        # LangChain 1.x returns messages.
        messages = response.get("messages", [])

        if messages:
            output = messages[-1].content
        else:
            output = str(response)

        results.append(
            {
                "app": app["name"],
                "output": output
            }
        )

    except Exception as e:
        results.append(
            {
                "app": app["name"],
                "error": str(e)
            }
        )


# --------------------------------------------------
# Save results
# --------------------------------------------------
with open(
    "results.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        results,
        f,
        indent=2,
        ensure_ascii=False
    )


print("Agent finished! Check results.json")
