from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import PyPDF2
from docx import Document as DocxDocument


class DocumentProcessor:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )


    def _chunk_text(self, file_path: str, text: str, doc_type: str) -> List[Document]:
        """Split text into chunks"""
        # Create documents with metadata
        return self.text_splitter.create_documents(
            [text],
            metadatas=[{"source": file_path, "type": doc_type}],
        )

    def process_pdf(self, file_path: str) -> List[Document]:
        """Extract text from a PDF file and split it into chunks"""
        reader = PyPDF2.PdfReader(file_path)
        text = ""
        for page_num, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += f"\n---- Page {page_num + 1} ----\n{page_text}"
        return self._chunk_text(file_path, text, "pdf")


    def process_docx(self, file_path: str) -> List[Document]:
        """Extract text from a DOCX file and split it into chunks"""
        doc = DocxDocument(file_path)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return self._chunk_text(file_path, text, "docx")
        

    def process_txt(self, file_path: str) -> List[Document]:
        """Process raw text into chunks"""
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return self._chunk_text(file_path, text, "txt")
    