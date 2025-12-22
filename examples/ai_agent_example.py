"""
Example: Basic AI Agent Usage with OLLAMA

This example demonstrates how to use the AI Agent for various tasks:
- Basic chat/conversation
- Multi-step reasoning
- Text summarization
- Sentiment analysis
- Information extraction
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents import AIAgent
from utils import check_ollama_availability


def main():
    """Demonstrate AI Agent capabilities."""
    
    print("=" * 60)
    print("AI Agent Example - OLLAMA & LangChain")
    print("=" * 60)
    
    # Check if OLLAMA is available
    if not check_ollama_availability():
        print("\n⚠️  WARNING: OLLAMA service not detected at http://localhost:11434")
        print("Please make sure OLLAMA is installed and running.")
        print("Visit: https://ollama.ai/")
        print("\nThis example will continue but may fail without OLLAMA.\n")
    
    # Initialize AI Agent
    print("\n1. Initializing AI Agent...")
    agent = AIAgent(
        model="llama2",  # Change to your preferred model
        temperature=0.7,
        verbose=False
    )
    print("✓ Agent initialized successfully!")
    
    # Example 1: Basic Chat
    print("\n" + "=" * 60)
    print("Example 1: Basic Chat")
    print("=" * 60)
    
    questions = [
        "What is artificial intelligence?",
        "Can you explain what you just said in simpler terms?",
        "What are some real-world applications?"
    ]
    
    for question in questions:
        print(f"\n👤 User: {question}")
        response = agent.chat(question)
        print(f"🤖 Agent: {response}")
    
    # Clear memory for next example
    agent.clear_memory()
    
    # Example 2: Multi-step Reasoning
    print("\n" + "=" * 60)
    print("Example 2: Multi-step Reasoning")
    print("=" * 60)
    
    task = "How can we reduce carbon emissions in urban areas?"
    print(f"\n📋 Task: {task}")
    reasoning = agent.reason(task)
    print(f"\n🤖 Agent Reasoning:\n{reasoning}")
    
    # Example 3: Text Summarization
    print("\n" + "=" * 60)
    print("Example 3: Text Summarization")
    print("=" * 60)
    
    long_text = """
    Artificial Intelligence (AI) has become one of the most transformative technologies 
    of the 21st century. It encompasses machine learning, deep learning, natural language 
    processing, and computer vision. AI systems can now perform tasks that traditionally 
    required human intelligence, such as recognizing speech, identifying images, making 
    decisions, and translating languages. The technology is being applied across various 
    industries including healthcare, finance, transportation, and entertainment. However, 
    the rapid advancement of AI also raises important ethical questions about privacy, 
    job displacement, and the need for responsible AI development.
    """
    
    print(f"\n📄 Original Text ({len(long_text.split())} words):")
    print(long_text.strip())
    
    summary = agent.summarize(long_text, max_length=50)
    print(f"\n📝 Summary:\n{summary}")
    
    # Example 4: Sentiment Analysis
    print("\n" + "=" * 60)
    print("Example 4: Sentiment Analysis")
    print("=" * 60)
    
    texts_to_analyze = [
        "I absolutely love this product! It exceeded all my expectations.",
        "The service was terrible and I'm very disappointed.",
        "It's okay, nothing special but it works as advertised."
    ]
    
    for text in texts_to_analyze:
        print(f"\n📄 Text: {text}")
        sentiment_result = agent.analyze_sentiment(text)
        print(f"😊 Sentiment: {sentiment_result['sentiment']}")
        print(f"💭 Explanation: {sentiment_result['explanation']}")
    
    # Example 5: Information Extraction
    print("\n" + "=" * 60)
    print("Example 5: Information Extraction")
    print("=" * 60)
    
    text_with_info = """
    John Smith met with Sarah Johnson at the New York office on January 15, 2024. 
    They discussed the upcoming project launch in San Francisco. The meeting was 
    also attended by Michael Chen from the London branch.
    """
    
    print(f"\n📄 Text:\n{text_with_info.strip()}")
    
    info_types = ["names", "locations", "dates"]
    for info_type in info_types:
        extracted = agent.extract_info(text_with_info, info_type)
        print(f"\n🔍 Extracted {info_type}:\n{extracted}")
    
    print("\n" + "=" * 60)
    print("✓ All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
