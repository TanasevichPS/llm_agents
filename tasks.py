# Researcher Agent Task
def researcher_task(researcher_agent, topic):
    print(f"Task: {researcher_agent.goal}")
    papers = researcher_agent.search_papers(topic)
    return papers

# Writer Agent Task
def writer_task(writer_agent, papers):
    print(f"Task: {writer_agent.goal}")
    summaries = writer_agent.summarize_papers(papers)
    return summaries
