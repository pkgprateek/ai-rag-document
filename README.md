---
title: AI Document Intelligence System (with RAG)
emoji: 📚
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.49.1
app_file: app/main.py
pinned: false
---

# AI Document Intelligence System

Upload documents and ask questions using advanced RAG (Retrieval-Augmented Generation) technology. Built with:
- **LangChain** for RAG orchestration
- **ChromaDB** for vector storage
- **BAAI/bge-small-en-v1.5** embeddings for superior retrieval quality
- **Meta Llama 3.2** via HuggingFace Inference API
- **Gradio** for interactive UI

## Features
- Interactive document processing (PDF, DOCX, TXT)
- Context-aware question answering with improved embeddings
- ⚡ Real-time processing and analysis
- Source citation for transparency
- Cloud-ready deployment on HuggingFace Spaces

## Setup

### 1. Get HuggingFace Token
1. Create a free account at [HuggingFace](https://huggingface.co/join)
2. Go to [Settings → Access Tokens](https://huggingface.co/settings/tokens)
3. Create a new token with **READ** access
4. Copy the token

### 2. Local Installation

```bash
# Clone the repository
git clone https://github.com/pkgprateek/ai-rag-document.git
cd ai-rag-document

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your HF_TOKEN

# Run the application
python app/main.py
```

### 3. Deploy to HuggingFace Spaces

1. **Fork or upload this repo to HuggingFace Spaces**
2. **Add your HF_TOKEN as a Space Secret:**
   - Go to your Space Settings → Repository secrets
   - Add a new secret: `HF_TOKEN` = your token
3. **Your app will automatically deploy!**

## Usage

1. Upload a PDF/DOCX/TXT file
2. Click "Process Document"
3. Get accurate answers with markdown formatting

## Technical Details

- **Embeddings**: BAAI/bge-small-en-v1.5 (significantly better than all-MiniLM-L6-v2)
- **LLM**: Meta Llama-3.2-3B-Instruct via HuggingFace Inference API
- **Vector Store**: ChromaDB with persistent storage
- **Chunking**: Smart text splitting with overlap for context preservation