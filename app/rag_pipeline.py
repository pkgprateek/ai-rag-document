from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain_community.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from typing import List

class RAGPipeline:
    def __init__(self, persist_directory: str = "./data/chroma_db"):
        #Initialize embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
        )
        #Initialize vector store
        self.vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embeddings,
        )
        #Initialize LLM 
        self.llm = Ollama(model="gemma3:latest")

        # Create RAG chain
        self.rag_chain = self.create_rag_chain()

    def create_rag_chain(self):
        """Create RAG chain"""
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
            Use the following pieces of retrieved context to answer the question at the end.
            You are an helpful assistant, so if you don't know the answer, just say that you don't know.
            Do not hallucinate. Do not make up information. Do not guess. Do not lie.
            Use factual information to answer the question. Verify the information you provide.
            Always cite the source of your answer in the format [Source: source_name]".
            
            Context: {context}

            Question: {question}

            Answer:
            """
        )

        self.rag_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(search_kwargs={"k": 4}),
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=True  # Fixed parameter name
        )
        return self.rag_chain  # Added return statement
    

    def add_documents(self, documents: List[Document]) -> None:
        """Add documents to the vector store"""
        self.vector_store.add_documents(documents)
        # In newer versions of langchain-chroma, persist() is no longer needed
        # as documents are automatically persisted when added

    
    def query(self, question: str) -> dict:
        """Query the RAG pipeline with a question"""
        result = self.rag_chain({"query": question})
        return {
            "answer": result["result"],
            "sources": result["source_documents"]
        }
