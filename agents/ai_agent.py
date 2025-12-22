"""
AI Agent using OLLAMA and LangChain
This module provides a flexible AI agent that can perform various tasks using local LLMs via OLLAMA.
"""

import os
from typing import List, Dict, Optional, Any
from langchain_community.llms import Ollama
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain


class AIAgent:
    """
    A customizable AI Agent powered by OLLAMA and LangChain.
    
    This agent can:
    - Answer questions and perform reasoning tasks
    - Maintain conversation context
    - Use custom tools and functions
    - Execute multi-step workflows
    """
    
    def __init__(
        self,
        model: str = "llama2",
        base_url: str = "http://localhost:11434",
        temperature: float = 0.7,
        verbose: bool = False
    ):
        """
        Initialize the AI Agent.
        
        Args:
            model: OLLAMA model name (e.g., 'llama2', 'mistral', 'codellama')
            base_url: OLLAMA API base URL
            temperature: Sampling temperature (0.0 to 1.0)
            verbose: Enable verbose logging
        """
        self.model = model
        self.base_url = base_url
        self.temperature = temperature
        self.verbose = verbose
        
        # Initialize OLLAMA LLM
        self.llm = Ollama(
            model=model,
            base_url=base_url,
            temperature=temperature
        )
        
        # Initialize conversation memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Custom tools for the agent
        self.tools: List[Tool] = []
        
    def add_tool(self, name: str, func: callable, description: str):
        """
        Add a custom tool to the agent.
        
        Args:
            name: Tool name
            func: Function to execute
            description: Tool description for the agent
        """
        tool = Tool(
            name=name,
            func=func,
            description=description
        )
        self.tools.append(tool)
        
    def chat(self, message: str) -> str:
        """
        Have a conversation with the AI agent.
        
        Args:
            message: User message
            
        Returns:
            Agent response
        """
        prompt = PromptTemplate(
            input_variables=["message", "chat_history"],
            template="""You are a helpful AI assistant. Use the conversation history to provide context-aware responses.

Chat History:
{chat_history}

Current Message: {message}

Response:"""
        )
        
        chain = LLMChain(
            llm=self.llm,
            prompt=prompt,
            memory=self.memory,
            verbose=self.verbose
        )
        
        response = chain.predict(message=message)
        return response.strip()
    
    def reason(self, task: str) -> str:
        """
        Perform multi-step reasoning on a task.
        
        Args:
            task: Task description
            
        Returns:
            Reasoning result
        """
        prompt = PromptTemplate(
            input_variables=["task"],
            template="""You are an AI agent capable of step-by-step reasoning. 
Break down the following task and provide a detailed solution:

Task: {task}

Think through this step by step:
1. First, analyze the task
2. Break it into sub-problems
3. Solve each sub-problem
4. Combine the solutions

Response:"""
        )
        
        chain = LLMChain(llm=self.llm, prompt=prompt, verbose=self.verbose)
        response = chain.predict(task=task)
        return response.strip()
    
    def summarize(self, text: str, max_length: int = 200) -> str:
        """
        Summarize a given text.
        
        Args:
            text: Text to summarize
            max_length: Maximum summary length
            
        Returns:
            Summary
        """
        prompt = PromptTemplate(
            input_variables=["text", "max_length"],
            template="""Summarize the following text in approximately {max_length} words or less:

Text: {text}

Summary:"""
        )
        
        chain = LLMChain(llm=self.llm, prompt=prompt, verbose=self.verbose)
        response = chain.predict(text=text, max_length=max_length)
        return response.strip()
    
    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """
        Analyze the sentiment of a given text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Sentiment analysis result
        """
        prompt = PromptTemplate(
            input_variables=["text"],
            template="""Analyze the sentiment of the following text. 
Respond with: POSITIVE, NEGATIVE, or NEUTRAL, followed by a brief explanation.

Text: {text}

Sentiment:"""
        )
        
        chain = LLMChain(llm=self.llm, prompt=prompt, verbose=self.verbose)
        response = chain.predict(text=text)
        
        lines = response.strip().split('\n')
        sentiment = lines[0].strip().upper()
        explanation = ' '.join(lines[1:]).strip() if len(lines) > 1 else ""
        
        return {
            "sentiment": sentiment,
            "explanation": explanation,
            "raw_response": response.strip()
        }
    
    def extract_info(self, text: str, info_type: str) -> str:
        """
        Extract specific information from text.
        
        Args:
            text: Source text
            info_type: Type of information to extract (e.g., 'names', 'dates', 'locations')
            
        Returns:
            Extracted information
        """
        prompt = PromptTemplate(
            input_variables=["text", "info_type"],
            template="""Extract all {info_type} from the following text:

Text: {text}

Extracted {info_type}:"""
        )
        
        chain = LLMChain(llm=self.llm, prompt=prompt, verbose=self.verbose)
        response = chain.predict(text=text, info_type=info_type)
        return response.strip()
    
    def clear_memory(self):
        """Clear conversation history."""
        self.memory.clear()
