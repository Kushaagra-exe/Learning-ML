from crewai import Task
from agents import blog_research, blog_writer
from tools import yt_tool


# Research Task
research_task = Task(
    description=(
        "Identify the video {topic}"
        "Get the detailed information about the video from the channel"
    ),
    expected_output="A compprehensive 3 paragraph long report based on {topic} of video from the channel ",
    tools=[yt_tool],
    agent=blog_research
)

# Blog writing task

writing_task = Task(
    description=("Get the information from the yt channel on topic {topic}"),
    expected_output="Summarise the information from the youtube channel video on the topic {topic} and create the content for the blog",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="blog-post.md"
)