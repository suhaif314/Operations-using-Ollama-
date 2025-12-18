"""
OCR Agent using OLLAMA and LangChain with Vision Capabilities
This module provides OCR functionality combined with AI analysis using OLLAMA.
"""

import os
from typing import List, Dict, Optional, Any, Union
from pathlib import Path
import pytesseract
from PIL import Image
import cv2
import numpy as np
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


class OCRAgent:
    """
    An OCR Agent that combines Tesseract OCR with OLLAMA AI for intelligent document processing.
    
    This agent can:
    - Extract text from images and documents
    - Preprocess images for better OCR accuracy
    - Analyze and summarize extracted text using AI
    - Handle multiple image formats (PNG, JPG, TIFF, etc.)
    - Process PDF documents
    """
    
    def __init__(
        self,
        model: str = "llama2",
        base_url: str = "http://localhost:11434",
        tesseract_path: Optional[str] = None,
        language: str = "eng",
        verbose: bool = False
    ):
        """
        Initialize the OCR Agent.
        
        Args:
            model: OLLAMA model name for text analysis
            base_url: OLLAMA API base URL
            tesseract_path: Path to Tesseract executable (optional)
            language: OCR language code (default: 'eng')
            verbose: Enable verbose logging
        """
        self.model = model
        self.base_url = base_url
        self.language = language
        self.verbose = verbose
        
        # Set Tesseract path if provided
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
        
        # Initialize OLLAMA LLM for text analysis
        self.llm = Ollama(
            model=model,
            base_url=base_url,
            temperature=0.3  # Lower temperature for more consistent analysis
        )
        
    def preprocess_image(
        self,
        image: Union[str, np.ndarray, Image.Image],
        enhance: bool = True
    ) -> np.ndarray:
        """
        Preprocess image to improve OCR accuracy.
        
        Args:
            image: Image path, numpy array, or PIL Image
            enhance: Apply enhancement techniques
            
        Returns:
            Preprocessed image as numpy array
        """
        # Load image if path is provided
        if isinstance(image, str):
            img = cv2.imread(image)
        elif isinstance(image, Image.Image):
            img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        else:
            img = image
        
        if img is None:
            raise ValueError("Failed to load image")
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        if enhance:
            # Apply denoising
            denoised = cv2.fastNlMeansDenoising(gray)
            
            # Apply adaptive thresholding
            processed = cv2.adaptiveThreshold(
                denoised,
                255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,
                11,
                2
            )
        else:
            processed = gray
        
        return processed
    
    def extract_text(
        self,
        image: Union[str, np.ndarray, Image.Image],
        preprocess: bool = True,
        config: str = ""
    ) -> str:
        """
        Extract text from an image using OCR.
        
        Args:
            image: Image path, numpy array, or PIL Image
            preprocess: Apply preprocessing
            config: Custom Tesseract configuration
            
        Returns:
            Extracted text
        """
        if preprocess:
            processed_img = self.preprocess_image(image)
        else:
            if isinstance(image, str):
                processed_img = cv2.imread(image)
            elif isinstance(image, Image.Image):
                processed_img = np.array(image)
            else:
                processed_img = image
        
        # Perform OCR
        text = pytesseract.image_to_string(
            processed_img,
            lang=self.language,
            config=config
        )
        
        return text.strip()
    
    def extract_text_with_confidence(
        self,
        image: Union[str, np.ndarray, Image.Image],
        preprocess: bool = True
    ) -> Dict[str, Any]:
        """
        Extract text with OCR confidence scores.
        
        Args:
            image: Image path, numpy array, or PIL Image
            preprocess: Apply preprocessing
            
        Returns:
            Dictionary with text and confidence data
        """
        if preprocess:
            processed_img = self.preprocess_image(image)
        else:
            if isinstance(image, str):
                processed_img = cv2.imread(image)
            elif isinstance(image, Image.Image):
                processed_img = np.array(image)
            else:
                processed_img = image
        
        # Get detailed OCR data
        data = pytesseract.image_to_data(
            processed_img,
            lang=self.language,
            output_type=pytesseract.Output.DICT
        )
        
        # Extract text with confidence
        text_parts = []
        confidences = []
        
        for i, conf in enumerate(data['conf']):
            if int(conf) > 0:  # Only include recognized text
                text_parts.append(data['text'][i])
                confidences.append(int(conf))
        
        full_text = ' '.join(text_parts)
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0
        
        return {
            "text": full_text.strip(),
            "confidence": avg_confidence,
            "word_count": len(text_parts),
            "details": data
        }
    
    def analyze_extracted_text(self, text: str, analysis_type: str = "summary") -> str:
        """
        Analyze extracted text using OLLAMA AI.
        
        Args:
            text: Extracted text to analyze
            analysis_type: Type of analysis ('summary', 'key_points', 'entities', 'classification')
            
        Returns:
            Analysis result
        """
        templates = {
            "summary": """Provide a concise summary of the following text:

Text: {text}

Summary:""",
            "key_points": """Extract the key points from the following text:

Text: {text}

Key Points:""",
            "entities": """Extract named entities (people, organizations, locations, dates) from the following text:

Text: {text}

Entities:""",
            "classification": """Classify the type of document this text is from (e.g., invoice, letter, form, receipt):

Text: {text}

Document Type:"""
        }
        
        template = templates.get(analysis_type, templates["summary"])
        prompt = PromptTemplate(input_variables=["text"], template=template)
        
        chain = LLMChain(llm=self.llm, prompt=prompt, verbose=self.verbose)
        response = chain.predict(text=text)
        
        return response.strip()
    
    def process_document(
        self,
        image_path: str,
        analyze: bool = True,
        analysis_type: str = "summary"
    ) -> Dict[str, Any]:
        """
        Complete document processing pipeline.
        
        Args:
            image_path: Path to image file
            analyze: Perform AI analysis on extracted text
            analysis_type: Type of analysis to perform
            
        Returns:
            Complete processing result
        """
        # Extract text with confidence
        ocr_result = self.extract_text_with_confidence(image_path)
        
        result = {
            "image_path": image_path,
            "extracted_text": ocr_result["text"],
            "confidence": ocr_result["confidence"],
            "word_count": ocr_result["word_count"]
        }
        
        # Perform AI analysis if requested
        if analyze and ocr_result["text"]:
            result["analysis"] = self.analyze_extracted_text(
                ocr_result["text"],
                analysis_type
            )
        
        return result
    
    def batch_process(
        self,
        image_paths: List[str],
        analyze: bool = True,
        analysis_type: str = "summary"
    ) -> List[Dict[str, Any]]:
        """
        Process multiple documents.
        
        Args:
            image_paths: List of image file paths
            analyze: Perform AI analysis on extracted text
            analysis_type: Type of analysis to perform
            
        Returns:
            List of processing results
        """
        results = []
        for image_path in image_paths:
            try:
                result = self.process_document(image_path, analyze, analysis_type)
                results.append(result)
            except Exception as e:
                results.append({
                    "image_path": image_path,
                    "error": str(e)
                })
        
        return results
    
    def extract_structured_data(self, text: str, fields: List[str]) -> Dict[str, str]:
        """
        Extract structured data fields from text using AI.
        
        Args:
            text: Source text
            fields: List of field names to extract
            
        Returns:
            Dictionary of extracted fields
        """
        fields_str = ", ".join(fields)
        prompt = PromptTemplate(
            input_variables=["text", "fields"],
            template="""Extract the following fields from the text: {fields}

Text: {text}

Respond in the format:
Field1: value1
Field2: value2

Extracted Data:"""
        )
        
        chain = LLMChain(llm=self.llm, prompt=prompt, verbose=self.verbose)
        response = chain.predict(text=text, fields=fields_str)
        
        # Parse response into dictionary
        result = {}
        for line in response.strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                result[key.strip()] = value.strip()
        
        return result
