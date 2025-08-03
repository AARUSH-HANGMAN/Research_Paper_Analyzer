from dotenv import load_dotenv
import os
from pypdf import PdfReader
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def summarize_pdf(pdf_path: str, question: str):
    pdf_text = extract_text_from_pdf(pdf_path)
    
    messages = [
        HumanMessage(content=f"Summarize this research paper for students:\n\n{pdf_text}\n\nQuestion: {question}\nProvide a clear, concise summary highlighting the main points of the paper.")
    ]

    llm = ChatOpenAI(
        temperature=0.7,
        model_name="gpt-3.5-turbo",
        openai_api_key=api_key
    )

    result = llm(messages)
    return result.content

if __name__ == "__main__":
    pdf_path = "sample_research_paper.pdf"  
    question = "What is the main contribution of this paper?"

    summary = summarize_pdf(pdf_path, question)
    print("\nPipeline Output:\n")
    print(summary)
