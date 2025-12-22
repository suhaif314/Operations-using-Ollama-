"""
Configuration utilities for OLLAMA agents
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv


def load_config() -> Dict[str, Any]:
    """
    Load configuration from environment variables.
    
    Returns:
        Configuration dictionary
    """
    # Load .env file if exists
    load_dotenv()
    
    config = {
        "ollama": {
            "base_url": os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
            "model": os.getenv("OLLAMA_MODEL", "llama2"),
        },
        "ocr": {
            "tesseract_path": os.getenv("TESSERACT_PATH", None),
            "language": os.getenv("OCR_LANGUAGE", "eng"),
        }
    }
    
    return config


def check_ollama_availability(base_url: str = "http://localhost:11434") -> bool:
    """
    Check if OLLAMA service is available.
    
    Args:
        base_url: OLLAMA API base URL
        
    Returns:
        True if available, False otherwise
    """
    import requests
    
    try:
        response = requests.get(f"{base_url}/api/tags", timeout=5)
        return response.status_code == 200
    except Exception:
        return False


def list_available_models(base_url: str = "http://localhost:11434") -> list:
    """
    List available OLLAMA models.
    
    Args:
        base_url: OLLAMA API base URL
        
    Returns:
        List of model names
    """
    import requests
    
    try:
        response = requests.get(f"{base_url}/api/tags", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return [model['name'] for model in data.get('models', [])]
        return []
    except Exception:
        return []
