# Test rag pipeline
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.rag_pipeline import RAGPipeline
from app.document_processor import DocumentProcessor
from dotenv import load_dotenv

load_dotenv()


processor = DocumentProcessor()
# chunks = processor.process_pdf("./data/test.pdf")
test_doc = """Python is a high-level programming language.
    It was created by Guido van Rossum in 1991.
    Python is known for its simple syntax., 
    test_python.txt"""
chunks = processor._chunk_text("user", test_doc, doc_type="txt")

# Initialize Rag and Using document processor
rag_pipeline = RAGPipeline()
rag_pipeline.add_documents(chunks)

# Query
question = "What is python known for?"
result = rag_pipeline.query(question)
print(f"Answer: {result['answer']}")


# Format sources with page numbers
# sources = result["sources_formatted"]
# source_info = []
# for i, doc in enumerate(sources, 1):
#     source_file = doc.metadata.get("source", "Unknown")
#     # Extract just filename
#     source_name = source_file.split("/")[-1] if "/" in source_file else source_file
#     page_preview = doc.page_content[:100].replace("\n", " ")
#     source_info.append(f"**[{i}]** {source_name}\n> {page_preview}...")

# sources_text = "\n\n".join(source_info) if source_info else "No sources found"
# print(f"Sources: {sources_text}")
