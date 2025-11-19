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

A production-ready document question-answering system built with Retrieval-Augmented Generation (RAG). Upload documents and query them using natural language with citation-backed responses.

## Architecture

This system implements a complete RAG pipeline with the following components:

**Document Processing**
- Multi-format support (PDF, DOCX, TXT)
- Intelligent text chunking with configurable overlap (1000 chars, 200 overlap)
- Preserves document structure with metadata tracking

**Retrieval System**
- Vector embeddings using BAAI/bge-small-en-v1.5 (384 dimensions)
- ChromaDB persistent vector store
- Top-k retrieval (k=4) with semantic similarity search
- Cosine similarity with L2 normalization

**Generation**
- Google Gemma 3-4B-IT via OpenRouter free tier
- Temperature: 0.1 for consistent, factual responses
- Max tokens: 512 for concise answers
- Hallucination prevention through strict context grounding

**Rate Limiting**
- 10 queries per hour tracked via filesystem-based state
- Prevents API abuse while maintaining usability

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Framework | LangChain 1.0.7 | RAG orchestration and chaining |
| Vector DB | ChromaDB 1.3.4 | Persistent vector storage |
| Embeddings | BAAI/bge-small-en-v1.5 | Semantic text representation |
| LLM | Google Gemma 3-4B-IT | Answer generation |
| UI | Gradio 5.49.1 | Interactive web interface |
| API | OpenRouter | Cost-free LLM access |

## Features

- Multi-format document ingestion with automatic format detection
- Context-aware question answering with source attribution
- Persistent vector storage (survives restarts)
- Rate limiting to prevent API abuse
- Markdown-formatted responses for readability
- Comprehensive error handling and validation
- Modular architecture for easy extension

---
## Local Development

### Prerequisites
- Python 3.10+
- pip or conda package manager
- OpenRouter API key (free tier available)

### Installation

```bash
# Clone repository
git clone https://github.com/pkgprateek/ai-rag-document.git
cd ai-rag-document

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your OPENROUTER_API_KEY
```

### Get OpenRouter API Key

1. Visit [OpenRouter](https://openrouter.ai/keys)
2. Sign up for a free account
3. Generate an API key
4. Add to `.env` file: `OPENROUTER_API_KEY=your_key_here`

### Run Application

```bash
python app/main.py
```

The application will start on `http://localhost:7860`


## Project Structure

```
ai-rag-document/
├── app/
│   ├── main.py                  # Gradio UI and application entry
│   ├── rag_pipeline.py          # RAG chain implementation
│   └── document_processor.py    # Document parsing and chunking
├── tests/
│   ├── test_rag_pipeline.py     # RAG pipeline tests
│   ├── test_document_processor.py
│   └── experiments.py           # Dev experiments
├── data/
│   ├── chroma_db/              # Vector DB persistence
│   └── rate_limit.json         # Query rate tracking
├── requirements.txt
├── .env.example
└── README.md
```

## Future Enhancements

- Multi-document cross-referencing
- Conversation history for follow-up questions
- Hybrid search (semantic + keyword)
- Advanced chunking strategies (semantic chunking)
- Support for images and tables (multimodal RAG)
- User authentication and document management

## License

This project is open source and available for portfolio and educational purposes.

## Contact

**Prateek Kumar Goel**
- GitHub: [@pkgprateek](https://github.com/pkgprateek)
- Project deployed on [Hugging Face Spaces](https://huggingface.co/spaces/pkgprateek)