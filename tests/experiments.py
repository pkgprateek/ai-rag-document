# Experimental code for testing RAG pipeline
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.rag_pipeline import RAGPipeline
from app.document_processor import DocumentProcessor
from dotenv import load_dotenv

load_dotenv()


# Example 1: Simple text test
def test_simple_query():
    processor = DocumentProcessor()

    test_doc = """Python is a high-level programming language.
    It was created by Guido van Rossum in 1991.
    Python is known for its simple syntax."""

    chunks = processor._chunk_text("test_doc.txt", test_doc, doc_type="txt")

    # Initialize RAG
    rag_pipeline = RAGPipeline()
    rag_pipeline.add_documents(chunks)

    # Query
    question = "What is python known for?"
    result = rag_pipeline.query(question)
    print(f"Question: {question}")
    print(f"Answer: {result['answer']}")
    print("\n" + "=" * 50 + "\n")


# Example 2: Testing with actual document
def test_with_pdf():
    processor = DocumentProcessor()
    rag_pipeline = RAGPipeline()

    # Process a PDF file
    pdf_path = "path/to/your/test.pdf"  # Replace with actual path
    if os.path.exists(pdf_path):
        chunks = processor.process_pdf(pdf_path)
        rag_pipeline.add_documents(chunks)

        question = "What is the main topic of this document?"
        result = rag_pipeline.query(question)
        print(f"Question: {question}")
        print(f"Answer: {result['answer']}")
    else:
        print(f"PDF not found: {pdf_path}")


# Example 3: Interactive testing
def interactive_test():
    processor = DocumentProcessor()
    rag_pipeline = RAGPipeline()

    # Add some test content
    test_doc = """Artificial Intelligence (AI) is transforming the world.
    Machine learning is a subset of AI that focuses on learning from data.
    Deep learning uses neural networks with multiple layers.
    Natural Language Processing (NLP) helps computers understand human language."""

    chunks = processor._chunk_text("ai_basics.txt", test_doc, doc_type="txt")
    rag_pipeline.add_documents(chunks)

    print("Interactive RAG Testing")
    print("Type 'quit' to exit\n")

    while True:
        question = input("Your question: ")
        if question.lower() == "quit":
            break

        try:
            result = rag_pipeline.query(question)
            print(f"Answer: {result['answer']}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
            break


if __name__ == "__main__":
    print("Running RAG Pipeline Experiments\n")

    # Run simple test
    test_simple_query()

    # Uncomment to run other tests
    # test_with_pdf()
    # interactive_test()
