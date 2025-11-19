from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import PyPDF2
from docx import Document as DocxDocument


class DocumentProcessor:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Initialize document processor with text splitting configuration.

        Args:
            chunk_size: Maximum characters per chunk (default: 1000)
            chunk_overlap: Characters to overlap between chunks (default: 200)
        """
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )

    def _chunk_text(self, file_path: str, text: str, doc_type: str) -> List[Document]:
        """
        Split text into overlapping chunks with metadata for better retrieval.

        Args:
            file_path: Original file path for metadata
            text: Text content to split
            doc_type: Document type (pdf/docx/txt)

        Returns:
            List[Document]: Chunked documents with metadata
        """
        # Create documents with metadata
        return self.text_splitter.create_documents(
            [text],
            metadatas=[{"source": file_path, "type": doc_type}],
        )

    def process_pdf(self, file_path: str) -> List[Document]:
        """
        Extract text from PDF file and convert to chunked documents.

        Args:
            file_path: Path to PDF file

        Returns:
            List[Document]: Processed document chunks
        """
        reader = PyPDF2.PdfReader(file_path)
        text = ""
        for page_num, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += f"\n---- Page {page_num + 1} ----\n{page_text}"
        return self._chunk_text(file_path, text, "pdf")

    def process_docx(self, file_path: str) -> List[Document]:
        """
        Extract text from DOCX file and convert to chunked documents.

        Args:
            file_path: Path to DOCX file

        Returns:
            List[Document]: Processed document chunks
        """
        doc = DocxDocument(file_path)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return self._chunk_text(file_path, text, "docx")

    def process_txt(self, file_path: str) -> List[Document]:
        """
        Read text file and convert to chunked documents.

        Args:
            file_path: Path to TXT file

        Returns:
            List[Document]: Processed document chunks
        """
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return self._chunk_text(file_path, text, "txt")
