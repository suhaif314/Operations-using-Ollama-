"""
OLLAMA Agents Package
Provides AI and OCR agents using OLLAMA and LangChain.
"""

from .ai_agent import AIAgent
from .ocr_agent import OCRAgent

__all__ = ['AIAgent', 'OCRAgent']
__version__ = '1.0.0'
