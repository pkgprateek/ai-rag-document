import gradio as gr
from rag_pipeline import RAGPipeline
from document_processor import DocumentProcessor
import os


class DocumentRagApp:
    def __init__(self):
        self.processor = DocumentProcessor()
        self.rag_pipeline = RAGPipeline()
        self.loaded_documents = []

    def process_document(self, file):
        """Process uplaoded document and add to RAG"""
        if file is None:
            return "Please upload a file."
        try:
            file_path = file.name
            file_name = os.path.basename(file_path)
            file_ext = os.path.splitext(file_path)[1].lower()

            # Check file type and process the file based on its extension:
            if file_ext == ".pdf":
                chunks = self.processor.process_pdf(file_path)
            elif file_ext == ".txt":
                chunks = self.processor.process_txt(file_path)
            elif file_ext == ".docx":
                chunks = self.processor.process_docx(file_path)
            else:
                return "Unsupported file type. Please upload a PDF, TXT, or DOCX file."

            self.rag_pipeline.add_documents(chunks)
            self.loaded_documents.append(file_name)
            return f"Processed {len(chunks)} chunks from '{file_name}'"
        except Exception as e:
            return f"Error processing file: {str(e)}"

    def ask_question(self, question):
        if not self.loaded_documents:
            return "Please upload and process a document before asking questions."

        if not question.strip():
            return "Please enter a question."

        try:
            result = self.rag_pipeline.query(question)
            answer = result["answer"]
            return answer
            # sources = result["sources"]
            # source_response = ""
            # for i, doc in enumerate(sources[:3], start=1):
            # src_name = doc.metadata.get("source", "Unknown Source")
            # content_preview = doc.page_content[:100] + "..."
            # source_response += f"\n{i}. {src_name}\n '{content_preview}'\n"
            # source_response += f"\n{i}. {content_preview}\n"
            # return answer, source_response
        except Exception as e:
            return f"Error answering question: {str(e)}"


# Initialize gradio App
app = DocumentRagApp()

# Create Gradio Interface
with gr.Blocks(title="AI Document QA System") as demo:
    gr.Markdown("AI Document QA System")
    gr.Markdown(
        "Uploade documents (PDF, DOCX, TXT) and talk to it with simple questions. Powered by RAG + LangChain."
    )

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 1. Upload a Document")
            file_upload = gr.File(
                label="Upload Document", file_types=[".pdf", ".docx", ".txt"]
            )
            process_btn = gr.Button("Process Document", variant="primary")
            process_response = gr.Textbox(label="Processing Status", lines=2)

            gr.Markdown("### 2. Ask Questions")
            question_input = gr.Textbox(
                label="Your Question",
                placeholder="Ask a question about the document...",
                lines=2,
            )
            ask_btn = gr.Button("Ask", variant="primary")

        with gr.Column(scale=2):
            gr.Markdown("### 3. Answer")

            answer_output = gr.Markdown(container=True, min_height="480px")
            # sources_output = gr.Markdown(
            #     label="Sources", container=True, min_height="120px"
            # )

        # Connect all functions
        process_btn.click(
            fn=app.process_document, inputs=[file_upload], outputs=[process_response]
        )

        ask_btn.click(
            fn=app.ask_question,
            inputs=[question_input],
            outputs=[answer_output],
            # outputs=[answer_output, sources_output],
        )

if __name__ == "__main__":
    demo.launch(share=True)
