from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv

load_dotenv()

vector_store = Chroma(
    collection_name="vishal_resume",
    embedding_function=GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    ),
    persist_directory="chroma_db",
)


def embed_add_to_vector_store(vector_store):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=150)

    pdfLoader = PyPDFLoader("data/Vishal's_Backend_Resume.pdf")
    pages = pdfLoader.load_and_split(
        text_splitter=text_splitter,
    )
    print(vector_store.add_documents(pages))
    print(vector_store.get(include=["embeddings", "documents", "metadatas"]))


docs = vector_store.similarity_search_with_score("What are my projects?", k=2)

for doc in docs:
    print("-----")
    print(doc)
