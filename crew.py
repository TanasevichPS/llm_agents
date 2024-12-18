from agent import researcher, writer
from tasks import researcher_task, writer_task

# Setup Crew of Agents
def run_crew(topic):
    # Researcher finds papers
    papers = researcher_task(researcher, topic)
    
    # Writer summarizes papers
    summaries = writer_task(writer, papers)
    
    return summaries

if __name__ == "__main__":
    topic = "AI in healthcare after 2022"
    result = run_crew(topic)
    
    print("\nFinal Summaries:")
    for summary in result:
        print(summary)
