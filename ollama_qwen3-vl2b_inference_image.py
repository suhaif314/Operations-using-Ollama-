import ollama
import os
import sys

# Ensure the image file path is correct
# Replace './image.jpg' with the actual path to your image file
image_path = r"C:\Users\DELL\OneDrive\Pictures\IMG_20211027_134936.jpg"
 

# Check if the image file exists
if not os.path.exists(image_path):
    print(f"Error: Image file '{image_path}' does not exist.")
    sys.exit(1)

# Prompt the model to describe the image
try:
    response = ollama.chat(
        model='qwen3-vl:2b',
        messages=[
            {
                'role': 'user',
                'content': 'Describe this image in detail.',
                'images': [image_path] # Pass the image path in a list
            }
        ],
        stream=False # Set to True for streaming responses
    )
    print(response['message']['content'])

except Exception as e:
    print(f"An error occurred: {e}")

