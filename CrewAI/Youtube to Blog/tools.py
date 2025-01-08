from crewai_tools import YoutubeChannelSearchTool
import os

# Initialize the tool to search within any Youtube channel's content the agent learns about during its execution
os.environ["OPENAI_API_KEY"] = "NA"

yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@FarahHawa')
