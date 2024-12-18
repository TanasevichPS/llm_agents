from tools import SerperDevTool

class ResearcherAgent:
    def __init__(self, name):
        self.name = name
        self.goal = "Find academic papers published after 2022"
        self.tool = SerperDevTool()  # Tool for web searching

    def search_papers(self, query):
        print(f"{self.name} is researching: {query}")
        return self.tool.search(query)

class WriterAgent:
    def __init__(self, name):
        self.name = name
        self.goal = "Compose a summary of the academic papers"
        self.tool = SerperDevTool()  # Tool for web searching
    
    def summarize_papers(self, papers):
        summaries = []
        for paper in papers:
            summary = self.tool.summarize(paper)
            summaries.append(summary)
        return summaries

# Initialize Google Generative AI Model (hypothetically)
class GoogleGenerativeAI:
    def __init__(self):
        print("Initializing Google Generative AI")

    def generate_summary(self, text):
        # Simulate summary generation
        return f"Summary of the article: {text[:100]}..."

# Instantiate AI
generative_ai = GoogleGenerativeAI()

# Setup Researcher and Writer Agents
researcher = ResearcherAgent("Dr. Paper Finder")
writer = WriterAgent("Prof. Paper Writer")
