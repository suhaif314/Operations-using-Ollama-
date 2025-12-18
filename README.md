# Operations using OLLAMA 🤖

Building Local AI Agents and OCR Agents using OLLAMA and LangChain for intelligent document processing and conversational AI.

## 🌟 Features

### AI Agent
- **Conversational AI**: Natural language chat with context awareness
- **Multi-step Reasoning**: Break down complex tasks and solve them step-by-step
- **Text Summarization**: Condense long texts into concise summaries
- **Sentiment Analysis**: Analyze emotions and opinions in text
- **Information Extraction**: Extract specific information like names, dates, and locations
- **Memory Management**: Maintain conversation history for context-aware responses

### OCR Agent
- **Text Extraction**: Extract text from images using Tesseract OCR
- **Image Preprocessing**: Enhance images for better OCR accuracy
- **AI-Powered Analysis**: Analyze extracted text using OLLAMA models
- **Structured Data Extraction**: Extract specific fields from documents
- **Batch Processing**: Process multiple documents efficiently
- **Confidence Scoring**: Get OCR confidence metrics
- **Document Classification**: Automatically classify document types

## 📋 Prerequisites

### 1. OLLAMA Installation
Install OLLAMA from [ollama.ai](https://ollama.ai/)

**Linux/macOS:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
Download the installer from the OLLAMA website.

**Pull a model:**
```bash
ollama pull llama2
# or other models like mistral, codellama, etc.
```

**Start OLLAMA service:**
```bash
ollama serve
```

### 2. Tesseract OCR Installation
For OCR functionality, install Tesseract:

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

**macOS:**
```bash
brew install tesseract
```

**Windows:**
Download from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

### 3. Python Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/suhaif314/Operations-using-Ollama-.git
cd Operations-using-Ollama-
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment (Optional)
```bash
cp .env.example .env
# Edit .env file to customize settings
```

### 4. Run Examples

**AI Agent Example:**
```bash
python examples/ai_agent_example.py
```

**OCR Agent Example:**
```bash
python examples/ocr_agent_example.py
```

## 💡 Usage Examples

### AI Agent

```python
from agents import AIAgent

# Initialize the agent
agent = AIAgent(model="llama2", temperature=0.7)

# Chat with the agent
response = agent.chat("What is machine learning?")
print(response)

# Multi-step reasoning
result = agent.reason("How can we solve climate change?")
print(result)

# Summarize text
summary = agent.summarize(long_text, max_length=100)
print(summary)

# Analyze sentiment
sentiment = agent.analyze_sentiment("I love this product!")
print(sentiment['sentiment'])  # POSITIVE

# Extract information
names = agent.extract_info(text, "names")
print(names)
```

### OCR Agent

```python
from agents import OCRAgent

# Initialize the agent
ocr_agent = OCRAgent(model="llama2", language="eng")

# Extract text from image
text = ocr_agent.extract_text("document.png")
print(text)

# Get OCR with confidence scores
result = ocr_agent.extract_text_with_confidence("document.png")
print(f"Confidence: {result['confidence']}%")
print(f"Text: {result['text']}")

# Complete document processing with AI analysis
result = ocr_agent.process_document(
    "invoice.png",
    analyze=True,
    analysis_type="summary"
)
print(result['extracted_text'])
print(result['analysis'])

# Extract structured data
fields = ["Invoice Number", "Date", "Total"]
data = ocr_agent.extract_structured_data(text, fields)
print(data)

# Batch processing
results = ocr_agent.batch_process(
    ["doc1.png", "doc2.png", "doc3.png"],
    analyze=True
)
```

## 🏗️ Project Structure

```
Operations-using-Ollama-/
├── agents/
│   ├── __init__.py
│   ├── ai_agent.py          # AI Agent implementation
│   └── ocr_agent.py         # OCR Agent implementation
├── examples/
│   ├── ai_agent_example.py  # AI Agent usage examples
│   └── ocr_agent_example.py # OCR Agent usage examples
├── utils/
│   ├── __init__.py
│   └── config.py            # Configuration utilities
├── requirements.txt         # Python dependencies
├── .env.example            # Example environment configuration
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🔧 Configuration

Create a `.env` file based on `.env.example`:

```env
# OLLAMA Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2

# OCR Configuration
TESSERACT_PATH=/usr/bin/tesseract
OCR_LANGUAGE=eng
```

## 📚 Available Models

OLLAMA supports various models. Popular choices:

- **llama2**: General-purpose, good balance
- **mistral**: Fast and efficient
- **codellama**: Optimized for code
- **phi**: Lightweight, fast inference
- **neural-chat**: Optimized for conversations
- **llava**: Vision-language model (for image understanding)

Pull models with:
```bash
ollama pull <model-name>
```

## 🎯 Use Cases

### AI Agent Use Cases
- **Customer Support**: Automated chatbot with context awareness
- **Content Generation**: Generate summaries, articles, or responses
- **Data Analysis**: Extract insights from text data
- **Research Assistant**: Multi-step reasoning for complex questions
- **Sentiment Monitoring**: Analyze customer feedback

### OCR Agent Use Cases
- **Invoice Processing**: Extract data from invoices automatically
- **Document Digitization**: Convert scanned documents to searchable text
- **Form Processing**: Extract structured data from forms
- **Receipt Analysis**: Parse receipt information
- **ID Card Reading**: Extract information from ID documents
- **Contract Analysis**: Extract key terms from contracts

## 🔬 Research & Development

This repository is designed for research and experimentation with:
- Local AI models using OLLAMA
- LangChain framework capabilities
- OCR and document processing pipelines
- Combining vision and language models
- Building custom AI agents for specific tasks

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Improve documentation
- Add new agent capabilities

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [OLLAMA](https://ollama.ai/) - Running LLMs locally
- [LangChain](https://python.langchain.com/) - Building AI applications
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - OCR engine
- [OpenCV](https://opencv.org/) - Image processing

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check the examples for usage patterns
- Review OLLAMA and LangChain documentation

## 🚀 Getting Started with Your Own Agents

To create custom agents:

1. **Extend the AI Agent**: Add custom tools and prompts
2. **Customize OCR Pipeline**: Add preprocessing steps or analysis types
3. **Combine Agents**: Create workflows that use both agents
4. **Experiment with Models**: Try different OLLAMA models for your use case

Happy building! 🎉
