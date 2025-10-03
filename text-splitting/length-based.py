from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


pdfLoader = PyPDFLoader('./data/Vishal\'s_Backend_Resume.pdf')
pdfDoc = pdfLoader.load()

text = """
Areas for Scrutiny / Potential Weaknesses (from my harsh perspective):
    "Backend Developer" Title - Lack of Seniority Indicators: While you have good technical contributions, your job titles are consistently "Backend Developer." For a "crucial" role requiring an "excellent" backend developer, I'd ideally see some leadership, mentorship, or architectural design responsibilities explicitly mentioned in your experience, even if it's within a smaller team. Are you just coding, or are you designing and owning significant components?
    Timeframes: Your experience at Fiel (Jan 2025 - June 2025) and your remote Espo role (July 2025 - Present) are quite short. While you've achieved things, it makes me wonder about your ability to see projects through longer cycles or handle the sustained challenges that come with a crucial role. The "August 2022 - Present" for Espo and "July 2025 - Present" for remote is a bit confusing. Clarify if the remote work is a continuation or a separate engagement.
    Impact vs. Description: While you've listed some quantifiable impacts (e.g., "reducing data latency by 30%"), some bullet points are still more descriptive than results-oriented. For a senior role, I want to see how you drove significant business or technical improvements.
    Scalability Depth: You mention "10K+ concurrent users" and "7K+ real-time notifications weekly." These are good, but for an "excellent" backend developer, I'd want to hear more about the challenges you faced at scale and how you specifically engineered solutions to overcome them. What trade-offs did you make? How did you ensure resilience?
    Testing: You list Jest and Mocha in your skills, but there's no mention of testing methodologies, test coverage, or how you ensured code quality in your project or work descriptions. For a crucial role, robust testing is non-negotiable.
    "Gemini" Mention: In "Interview AI," you mentioned "Implemented AI-driven question generation using gemini." While technically a tool, for a resume, it's more impactful to describe the logic and architecture around the AI integration rather than just naming the model. It's a minor point, but it shows a tendency to describe what you used rather than how you engineered.
    Kafka: You list Kafka in your skills, but there's no corresponding experience or project demonstrating its use. This is a red flag for me – if it's a crucial skill for the role, I'd expect to see practical application.
    DevOps Depth: Docker and Serverless are listed, but again, the descriptions lack depth. How have you leveraged these for deployment, scaling, or CI/CD?
"""


splitter = CharacterTextSplitter(
  chunk_size=400,
  chunk_overlap=20,
  separator=''
)

splitted_text = splitter.split_text(text)
splitted_doc = splitter.split_documents(pdfDoc)


for (i, r) in enumerate(splitted_doc):
  print(f"--- Chunk {i+1} ---")
  print(r)
  print()
