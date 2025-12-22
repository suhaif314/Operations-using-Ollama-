"""
Example: OCR Agent Usage with OLLAMA

This example demonstrates how to use the OCR Agent for document processing:
- Extract text from images
- Preprocess images for better OCR
- Analyze extracted text using AI
- Extract structured data from documents
"""

import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents import OCRAgent
from utils import check_ollama_availability


def create_sample_image(text: str, output_path: str):
    """
    Create a sample image with text for demonstration.
    
    Args:
        text: Text to write on image
        output_path: Path to save the image
    """
    # Create a white image
    img = Image.new('RGB', (800, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, fall back to default if not available
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    # Draw text
    draw.text((50, 50), text, fill='black', font=font)
    
    # Save image
    img.save(output_path)
    print(f"✓ Created sample image: {output_path}")


def main():
    """Demonstrate OCR Agent capabilities."""
    
    print("=" * 60)
    print("OCR Agent Example - OLLAMA & LangChain")
    print("=" * 60)
    
    # Check if OLLAMA is available
    if not check_ollama_availability():
        print("\n⚠️  WARNING: OLLAMA service not detected at http://localhost:11434")
        print("Please make sure OLLAMA is installed and running.")
        print("Visit: https://ollama.ai/")
        print("\nThis example will continue but AI analysis will fail without OLLAMA.\n")
    
    # Check if Tesseract is available
    try:
        import pytesseract
        pytesseract.get_tesseract_version()
        print("✓ Tesseract OCR is available")
    except:
        print("\n⚠️  WARNING: Tesseract OCR not detected")
        print("Please install Tesseract:")
        print("  Ubuntu/Debian: sudo apt-get install tesseract-ocr")
        print("  macOS: brew install tesseract")
        print("  Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki")
        print("\nThis example may fail without Tesseract.\n")
    
    # Create temp directory for sample images
    temp_dir = Path("/tmp/ocr_examples")
    temp_dir.mkdir(exist_ok=True)
    
    # Initialize OCR Agent
    print("\n1. Initializing OCR Agent...")
    ocr_agent = OCRAgent(
        model="llama2",  # Change to your preferred model
        language="eng",
        verbose=False
    )
    print("✓ OCR Agent initialized successfully!")
    
    # Example 1: Simple Text Extraction
    print("\n" + "=" * 60)
    print("Example 1: Simple Text Extraction")
    print("=" * 60)
    
    sample_text = """
    INVOICE
    
    Invoice Number: INV-2024-001
    Date: January 15, 2024
    
    Bill To:
    John Smith
    123 Main Street
    New York, NY 10001
    
    Item          Quantity    Price      Total
    Widget A      5           $10.00     $50.00
    Widget B      3           $15.00     $45.00
    
    Subtotal:                            $95.00
    Tax (8%):                            $7.60
    Total:                               $102.60
    """
    
    # Create sample invoice image
    sample_image_path = temp_dir / "sample_invoice.png"
    create_sample_image(sample_text, str(sample_image_path))
    
    print("\n📄 Extracting text from image...")
    extracted_text = ocr_agent.extract_text(str(sample_image_path))
    print(f"\n✓ Extracted Text:\n{extracted_text}")
    
    # Example 2: OCR with Confidence Scores
    print("\n" + "=" * 60)
    print("Example 2: OCR with Confidence Scores")
    print("=" * 60)
    
    ocr_result = ocr_agent.extract_text_with_confidence(str(sample_image_path))
    print(f"\n📊 OCR Statistics:")
    print(f"  - Confidence: {ocr_result['confidence']:.2f}%")
    print(f"  - Word Count: {ocr_result['word_count']}")
    print(f"  - Text Length: {len(ocr_result['text'])} characters")
    
    # Example 3: AI-Powered Text Analysis
    print("\n" + "=" * 60)
    print("Example 3: AI-Powered Text Analysis")
    print("=" * 60)
    
    if extracted_text.strip():
        print("\n📝 Analyzing extracted text...")
        
        # Summarize
        print("\n🔍 Summary:")
        summary = ocr_agent.analyze_extracted_text(extracted_text, "summary")
        print(summary)
        
        # Extract key points
        print("\n🔍 Key Points:")
        key_points = ocr_agent.analyze_extracted_text(extracted_text, "key_points")
        print(key_points)
        
        # Classify document type
        print("\n🔍 Document Classification:")
        classification = ocr_agent.analyze_extracted_text(extracted_text, "classification")
        print(classification)
    else:
        print("⚠️  No text extracted, skipping AI analysis")
    
    # Example 4: Complete Document Processing
    print("\n" + "=" * 60)
    print("Example 4: Complete Document Processing Pipeline")
    print("=" * 60)
    
    result = ocr_agent.process_document(
        str(sample_image_path),
        analyze=True,
        analysis_type="summary"
    )
    
    print(f"\n📄 Document: {result['image_path']}")
    print(f"📊 Confidence: {result['confidence']:.2f}%")
    print(f"📊 Word Count: {result['word_count']}")
    print(f"\n📝 Extracted Text Preview:")
    print(result['extracted_text'][:200] + "..." if len(result['extracted_text']) > 200 else result['extracted_text'])
    
    if 'analysis' in result:
        print(f"\n🤖 AI Analysis:")
        print(result['analysis'])
    
    # Example 5: Structured Data Extraction
    print("\n" + "=" * 60)
    print("Example 5: Structured Data Extraction")
    print("=" * 60)
    
    if extracted_text.strip():
        fields = ["Invoice Number", "Date", "Total Amount", "Customer Name"]
        print(f"\n🔍 Extracting fields: {', '.join(fields)}")
        
        structured_data = ocr_agent.extract_structured_data(extracted_text, fields)
        print("\n✓ Extracted Structured Data:")
        for field, value in structured_data.items():
            print(f"  - {field}: {value}")
    
    # Example 6: Batch Processing
    print("\n" + "=" * 60)
    print("Example 6: Batch Processing Multiple Documents")
    print("=" * 60)
    
    # Create multiple sample images
    sample_texts = [
        "Document 1: This is a simple test document.",
        "Document 2: Another sample with different content.",
        "Document 3: Third document for batch processing."
    ]
    
    sample_paths = []
    for i, text in enumerate(sample_texts, 1):
        path = temp_dir / f"sample_{i}.png"
        create_sample_image(text, str(path))
        sample_paths.append(str(path))
    
    print(f"\n📚 Processing {len(sample_paths)} documents...")
    batch_results = ocr_agent.batch_process(
        sample_paths,
        analyze=False  # Skip analysis for faster batch processing
    )
    
    for i, result in enumerate(batch_results, 1):
        if 'error' in result:
            print(f"\n❌ Document {i}: Error - {result['error']}")
        else:
            print(f"\n✓ Document {i}:")
            print(f"  - Confidence: {result['confidence']:.2f}%")
            print(f"  - Text: {result['extracted_text'][:50]}...")
    
    print("\n" + "=" * 60)
    print("✓ All OCR examples completed!")
    print(f"📁 Sample images saved in: {temp_dir}")
    print("=" * 60)


if __name__ == "__main__":
    main()
