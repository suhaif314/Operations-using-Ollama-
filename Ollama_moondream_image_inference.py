import ollama
image_path = r"C:\Self_Coding\DATA\invoice.png"
 
# Inference using a local image path
response = ollama.chat(
    model='moondream:1.8b',
    messages=[{
        'role': 'user',
        'content': 'What is the date in this image?',
        'images': [image_path]  # List of image paths
    }]
)

print(response.message.content)
