from crewai import Agent, LLM
from tools import yt_tool
from langchain_openai import ChatOpenAI
import os

llm = LLM(
    model = "ollama/gemma2:2b",
    base_url = "http://localhost:11434"
)



blog_research = Agent(
    role="Research content of YT videos",
    goal="Get the relevant vid content of topic {topic} from YT",
    verbose=True,
    memory=True,
    backstory=("Expert in understanding yt videos"),
    allow_delegation=True,
    tools=[yt_tool],
    llm=llm
)

blog_writer = Agent(
    role="Write Blogs",
    goal="Narrate a good story about the video {topic} from YT",
    backstory=(
        "With flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner"
    ),
    tools=[yt_tool],
    allow_delegation=False,
    llm=llm


)