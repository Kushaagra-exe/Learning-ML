from crewai import Crew, Process
from agents import blog_writer, blog_research
from tasks import research_task, writing_task


crew = Crew(
    agents=[blog_research, blog_writer],
    tasks=[writing_task, research_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)


result = crew.kickoff(inputs={"topic":"Finding IDORs"})
print(result)