from main import summarize_pdf

pdf_path = "sample_research_paper.pdf"  
question = "What is the main contribution of this paper?"

summary = summarize_pdf(pdf_path, question)
print("\nCrewAI Output:\n")
print(summary)
