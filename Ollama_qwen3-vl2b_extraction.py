import ollama
import os
import sys
import time
import json

# Ensure the image file path is correct
# Replace with the actual path to your invoice image file
image_path = r"C:\Self_Coding\DATA\invoice.png"
 

# Check if the image file exists
if not os.path.exists(image_path):
    print(f"Error: Image file '{image_path}' does not exist.")
    sys.exit(1)

# OCR prompt for invoice extraction
ocr_prompt = """You are an OCR system specialized in extracting invoice data. 
Analyze this invoice image and extract ALL text and data with high accuracy.

Please extract and structure the following information:

1. **Invoice Header:**
   - Invoice Number
   - Invoice Date
   - Due Date
   - PO Number (if any)

2. **Vendor/Seller Details:**
   - Company Name
   - Address
   - Phone/Email
   - Tax ID/VAT Number

3. **Customer/Buyer Details:**
   - Company/Customer Name
   - Billing Address
   - Shipping Address (if different)

4. **Line Items (for each item):**
   - Item Number/SKU
   - Description
   - Quantity
   - Unit Price
   - Tax/VAT
   - Line Total

5. **Totals:**
   - Subtotal
   - Tax Amount
   - Discount (if any)
   - Shipping/Handling (if any)
   - Grand Total

6. **Payment Information:**
   - Payment Terms
   - Bank Details (if visible)
   - Payment Methods accepted

7. **Additional Notes:**
   - Any other text or notes visible on the invoice

Extract ALL visible text exactly as it appears. If a field is not visible or not applicable, mark it as "N/A".
Format the output in a clear, structured manner."""

# Prompt the model to extract invoice contents from the image
try:
    # Start timing
    start_time = time.time()
    
    print("=" * 60)
    print("INVOICE OCR EXTRACTION")
    print("=" * 60)
    print(f"Processing image: {image_path}")
    print("-" * 60)
    
    response = ollama.chat(
        model='qwen3-vl:2b',
        messages=[
            {
                'role': 'user',
                'content': ocr_prompt,
                'images': [image_path]
            }
        ],
        stream=False
    )
    
    # End timing
    end_time = time.time()
    processing_time = end_time - start_time
    
    # Print extracted content
    print("\n📄 EXTRACTED INVOICE DATA:\n")
    print(response['message']['content'])
    
    print("\n" + "=" * 60)
    print(f"⏱️  Processing Time: {processing_time:.2f} seconds")
    print("=" * 60)

except Exception as e:
    print(f"An error occurred: {e}")

