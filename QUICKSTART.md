# Quick Start Guide

This guide will help you get started with the AI and OCR agents in just a few minutes.

## 🚀 Installation Steps

### Step 1: Install OLLAMA

**Linux/macOS:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
Download and install from [ollama.ai](https://ollama.ai/)

### Step 2: Pull a Model

```bash
# Start OLLAMA (if not already running)
ollama serve

# In a new terminal, pull a model
ollama pull llama2
```

You can also try other models:
```bash
ollama pull mistral    # Fast and efficient
ollama pull phi        # Lightweight
ollama pull codellama  # For code-related tasks
```

### Step 3: Install Tesseract (for OCR)

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
Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)

### Step 4: Install Python Dependencies

```bash
# Clone the repository
git clone https://github.com/suhaif314/Operations-using-Ollama-.git
cd Operations-using-Ollama-

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🎯 Quick Test

### Test 1: Verify OLLAMA is Working

```bash
# Check OLLAMA is running
curl http://localhost:11434/api/tags

# Test a simple prompt
ollama run llama2 "What is AI?"
```

### Test 2: Run AI Agent Example

```bash
python examples/ai_agent_example.py
```

This will demonstrate:
- Basic chat functionality
- Multi-step reasoning
- Text summarization
- Sentiment analysis
- Information extraction

### Test 3: Run OCR Agent Example

```bash
python examples/ocr_agent_example.py
```

This will demonstrate:
- Text extraction from images
- OCR confidence scoring
- AI-powered text analysis
- Structured data extraction
- Batch processing

### Test 4: Run Advanced Workflow

```bash
python examples/advanced_workflow.py
```

This combines both agents to show:
- Complete document processing pipelines
- Cross-document analysis
- Intelligent routing and classification

## 📝 Your First Custom Script

Create a file `my_agent.py`:

```python
from agents import AIAgent, OCRAgent

# Initialize agents
ai_agent = AIAgent(model="llama2")
ocr_agent = OCRAgent(model="llama2")

# Use AI agent
response = ai_agent.chat("Explain machine learning in simple terms")
print("AI Response:", response)

# Use OCR agent (you need an image file)
# text = ocr_agent.extract_text("path/to/your/image.png")
# print("Extracted Text:", text)
```

Run it:
```bash
python my_agent.py
```

## 🔧 Configuration

Create a `.env` file for custom configuration:

```bash
cp .env.example .env
```

Edit `.env`:
```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2
TESSERACT_PATH=/usr/bin/tesseract
OCR_LANGUAGE=eng
```

## 📚 Common Use Cases

### 1. Document Processing
```python
from agents import OCRAgent

ocr = OCRAgent()
result = ocr.process_document("invoice.png", analyze=True)
print(f"Extracted: {result['extracted_text']}")
print(f"Summary: {result['analysis']}")
```

### 2. Chatbot
```python
from agents import AIAgent

agent = AIAgent()
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = agent.chat(user_input)
    print(f"Bot: {response}")
```

### 3. Data Extraction
```python
from agents import OCRAgent

ocr = OCRAgent()
text = ocr.extract_text("form.png")
fields = ["Name", "Date", "Amount"]
data = ocr.extract_structured_data(text, fields)
print(data)
```

## 🐛 Troubleshooting

### OLLAMA not responding
```bash
# Check if OLLAMA is running
ps aux | grep ollama

# Restart OLLAMA
ollama serve
```

### Import errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Tesseract not found
```bash
# Ubuntu/Debian
sudo apt-get install tesseract-ocr

# Check installation
tesseract --version
```

### Low memory issues
Use a smaller model:
```bash
ollama pull phi  # Much smaller than llama2
```

Then update your code:
```python
agent = AIAgent(model="phi")
```

## 🎓 Next Steps

1. **Read the main README.md** for comprehensive documentation
2. **Check RESEARCH_GUIDE.md** for advanced topics
3. **Explore the examples/** directory for more use cases
4. **Customize the agents** for your specific needs

## 💡 Tips

- Start with smaller models (phi, mistral) if you have limited resources
- Use temperature=0.0 for more deterministic outputs
- Preprocess images for better OCR accuracy
- Keep conversations focused for better AI responses
- Experiment with different prompts for optimal results

## 🆘 Getting Help

- Check the [OLLAMA documentation](https://github.com/ollama/ollama)
- Review [LangChain docs](https://python.langchain.com/)
- Open an issue on GitHub
- Review the example scripts for usage patterns

Happy coding! 🎉
