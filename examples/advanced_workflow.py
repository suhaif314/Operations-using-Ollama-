"""
Advanced Example: Combining AI and OCR Agents

This example demonstrates how to combine both agents for intelligent document processing workflows:
- Extract text from documents using OCR
- Analyze and process the text using AI
- Create a complete document understanding pipeline
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents import AIAgent, OCRAgent
from utils import check_ollama_availability


def create_business_card(output_path: str):
    """Create a sample business card image."""
    img = Image.new('RGB', (600, 350), color='white')
    draw = ImageDraw.Draw(img)
    
    # Add border
    draw.rectangle([(10, 10), (590, 340)], outline='black', width=2)
    
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except:
        font_large = font_medium = font_small = ImageFont.load_default()
    
    # Draw business card content
    draw.text((50, 40), "JOHN SMITH", fill='black', font=font_large)
    draw.text((50, 80), "Senior Software Engineer", fill='gray', font=font_medium)
    draw.line([(50, 120), (550, 120)], fill='black', width=1)
    
    draw.text((50, 150), "Email: john.smith@techcorp.com", fill='black', font=font_small)
    draw.text((50, 180), "Phone: +1 (555) 123-4567", fill='black', font=font_small)
    draw.text((50, 210), "Location: San Francisco, CA", fill='black', font=font_small)
    draw.text((50, 240), "LinkedIn: linkedin.com/in/johnsmith", fill='black', font=font_small)
    
    draw.text((50, 290), "TechCorp Solutions Inc.", fill='black', font=font_medium)
    
    img.save(output_path)
    print(f"✓ Created business card: {output_path}")


def create_receipt(output_path: str):
    """Create a sample receipt image."""
    img = Image.new('RGB', (500, 600), color='white')
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        font_normal = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
    except:
        font_title = font_normal = ImageFont.load_default()
    
    # Draw receipt content
    draw.text((150, 30), "TECH STORE", fill='black', font=font_title)
    draw.text((120, 60), "123 Market Street", fill='black', font=font_normal)
    draw.text((130, 85), "San Francisco, CA", fill='black', font=font_normal)
    draw.line([(50, 120), (450, 120)], fill='black', width=2)
    
    draw.text((50, 140), "Date: 2024-01-15", fill='black', font=font_normal)
    draw.text((50, 165), "Receipt #: 00123456", fill='black', font=font_normal)
    draw.line([(50, 200), (450, 200)], fill='black', width=1)
    
    # Items
    items = [
        ("Laptop", "$999.99"),
        ("Mouse", "$29.99"),
        ("Keyboard", "$79.99"),
        ("USB Cable", "$15.99"),
    ]
    
    y = 220
    for item, price in items:
        draw.text((50, y), item, fill='black', font=font_normal)
        draw.text((350, y), price, fill='black', font=font_normal)
        y += 30
    
    draw.line([(50, y + 10), (450, y + 10)], fill='black', width=1)
    
    # Total
    draw.text((50, y + 30), "Subtotal:", fill='black', font=font_normal)
    draw.text((350, y + 30), "$1,125.96", fill='black', font=font_normal)
    
    draw.text((50, y + 60), "Tax (8.5%):", fill='black', font=font_normal)
    draw.text((350, y + 60), "$95.71", fill='black', font=font_normal)
    
    draw.line([(50, y + 90), (450, y + 90)], fill='black', width=2)
    
    draw.text((50, y + 110), "TOTAL:", fill='black', font=font_title)
    draw.text((320, y + 110), "$1,221.67", fill='black', font=font_title)
    
    img.save(output_path)
    print(f"✓ Created receipt: {output_path}")


def main():
    """Demonstrate combined AI and OCR agent workflows."""
    
    print("=" * 70)
    print("Advanced Example: AI + OCR Agent Workflow")
    print("=" * 70)
    
    # Check prerequisites
    if not check_ollama_availability():
        print("\n⚠️  WARNING: OLLAMA service not detected")
        print("This example requires OLLAMA to be running.\n")
    
    # Create temp directory
    temp_dir = Path("/tmp/advanced_examples")
    temp_dir.mkdir(exist_ok=True)
    
    # Initialize both agents
    print("\n1. Initializing agents...")
    ai_agent = AIAgent(model="llama2", temperature=0.7)
    ocr_agent = OCRAgent(model="llama2", language="eng")
    print("✓ Both agents initialized!")
    
    # Workflow 1: Business Card Processing
    print("\n" + "=" * 70)
    print("Workflow 1: Intelligent Business Card Processing")
    print("=" * 70)
    
    # Create sample business card
    card_path = temp_dir / "business_card.png"
    create_business_card(str(card_path))
    
    # Step 1: Extract text using OCR
    print("\n📸 Step 1: Extracting text from business card...")
    card_text = ocr_agent.extract_text(str(card_path))
    print(f"✓ Extracted text:\n{card_text}\n")
    
    # Step 2: Extract structured contact information using OCR Agent
    print("📋 Step 2: Extracting structured data...")
    contact_fields = ["Name", "Title", "Email", "Phone", "Location", "Company"]
    contact_data = ocr_agent.extract_structured_data(card_text, contact_fields)
    
    print("✓ Structured contact information:")
    for field, value in contact_data.items():
        print(f"  - {field}: {value}")
    
    # Step 3: Use AI to generate a professional summary
    print("\n🤖 Step 3: Generating professional summary using AI...")
    summary_prompt = f"Based on this business card information, write a brief professional introduction:\n\n{card_text}"
    introduction = ai_agent.chat(summary_prompt)
    print(f"✓ Generated introduction:\n{introduction}")
    
    # Workflow 2: Receipt Analysis and Insights
    print("\n" + "=" * 70)
    print("Workflow 2: Receipt Analysis with Financial Insights")
    print("=" * 70)
    
    # Create sample receipt
    receipt_path = temp_dir / "receipt.png"
    create_receipt(str(receipt_path))
    
    # Step 1: Process receipt with OCR
    print("\n📸 Step 1: Processing receipt with OCR...")
    receipt_result = ocr_agent.process_document(
        str(receipt_path),
        analyze=True,
        analysis_type="key_points"
    )
    
    print(f"✓ OCR Confidence: {receipt_result['confidence']:.2f}%")
    print(f"✓ Extracted text:\n{receipt_result['extracted_text']}\n")
    
    if 'analysis' in receipt_result:
        print(f"📊 Key points identified:\n{receipt_result['analysis']}\n")
    
    # Step 2: Extract financial data
    print("💰 Step 2: Extracting financial details...")
    financial_fields = ["Date", "Receipt Number", "Subtotal", "Tax", "Total"]
    financial_data = ocr_agent.extract_structured_data(
        receipt_result['extracted_text'],
        financial_fields
    )
    
    print("✓ Financial details:")
    for field, value in financial_data.items():
        print(f"  - {field}: {value}")
    
    # Step 3: Use AI to categorize expenses and provide insights
    print("\n🤖 Step 3: AI-powered expense analysis...")
    analysis_prompt = f"""Analyze this receipt and provide:
1. Expense category
2. Budget recommendations
3. Any notable observations

Receipt details:
{receipt_result['extracted_text']}
"""
    
    expense_analysis = ai_agent.chat(analysis_prompt)
    print(f"✓ Expense analysis:\n{expense_analysis}")
    
    # Workflow 3: Multi-Document Intelligence
    print("\n" + "=" * 70)
    print("Workflow 3: Multi-Document Analysis with Cross-Referencing")
    print("=" * 70)
    
    # Combine information from both documents
    print("\n🔗 Analyzing relationship between documents...")
    
    combined_prompt = f"""I have two documents:

Document 1 (Business Card):
{card_text}

Document 2 (Receipt):
{receipt_result['extracted_text']}

Please answer:
1. Could this receipt belong to the person on the business card?
2. Is this a business expense?
3. What insights can you derive from having both documents?
"""
    
    cross_analysis = ai_agent.reason(combined_prompt)
    print(f"✓ Cross-document analysis:\n{cross_analysis}")
    
    # Workflow 4: Document Classification and Routing
    print("\n" + "=" * 70)
    print("Workflow 4: Automated Document Classification")
    print("=" * 70)
    
    documents = [
        (str(card_path), "Business Card"),
        (str(receipt_path), "Receipt")
    ]
    
    print("\n📂 Classifying documents...")
    for doc_path, expected_type in documents:
        # Extract text
        text = ocr_agent.extract_text(doc_path)
        
        # Classify using AI
        classification = ocr_agent.analyze_extracted_text(text, "classification")
        
        print(f"\n✓ Document: {Path(doc_path).name}")
        print(f"  Expected: {expected_type}")
        print(f"  Classified as: {classification}")
    
    # Workflow 5: Intelligent Data Extraction Pipeline
    print("\n" + "=" * 70)
    print("Workflow 5: Complete Document Processing Pipeline")
    print("=" * 70)
    
    print("\n🔄 Running complete pipeline...")
    
    def process_document_pipeline(image_path: str, doc_type: str):
        """Complete document processing pipeline."""
        print(f"\n📄 Processing {doc_type}...")
        
        # OCR extraction
        result = ocr_agent.process_document(image_path, analyze=False)
        print(f"  ✓ Text extracted (confidence: {result['confidence']:.2f}%)")
        
        # AI classification
        doc_class = ocr_agent.analyze_extracted_text(result['extracted_text'], "classification")
        print(f"  ✓ Classified as: {doc_class.split(':')[-1].strip()}")
        
        # Extract key information based on document type
        if "business card" in doc_class.lower() or doc_type == "Business Card":
            fields = ["Name", "Email", "Phone"]
        else:
            fields = ["Date", "Total", "Items"]
        
        structured = ocr_agent.extract_structured_data(result['extracted_text'], fields)
        print(f"  ✓ Extracted {len(structured)} structured fields")
        
        # Generate summary
        summary = ai_agent.summarize(result['extracted_text'], max_length=50)
        print(f"  ✓ Summary: {summary[:100]}...")
        
        return {
            "type": doc_class,
            "data": structured,
            "summary": summary
        }
    
    # Process all documents through pipeline
    pipeline_results = []
    for doc_path, doc_type in documents:
        result = process_document_pipeline(doc_path, doc_type)
        pipeline_results.append(result)
    
    print("\n" + "=" * 70)
    print("✓ All workflows completed successfully!")
    print(f"📁 Sample documents saved in: {temp_dir}")
    print("=" * 70)
    
    # Final summary
    print("\n📊 Summary of Capabilities Demonstrated:")
    print("  ✓ OCR text extraction with preprocessing")
    print("  ✓ Structured data extraction from documents")
    print("  ✓ AI-powered text analysis and summarization")
    print("  ✓ Document classification and routing")
    print("  ✓ Cross-document intelligence and insights")
    print("  ✓ Complete end-to-end document processing pipeline")
    print("\n🎉 This demonstrates the power of combining OCR and AI agents!")


if __name__ == "__main__":
    main()
