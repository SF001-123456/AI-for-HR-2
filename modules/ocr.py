import gradio as gr
from llm import ollama_llm
import easyocr

temp="""
summarise the receipt for me in term of
Name:
Location:
Date:
Phone:
Subtotal:
Tax:
Total Amount:
"""

def ocrImage(img):

    print("decoding image")
    reader = easyocr.Reader(['en'])   
    result_img = reader.readtext(img)
    print("result_img:" ,result_img)

    print("\n\ngenerating response")
    result = ollama_llm(temp,result_img)
    print("result: ",result)
 
    return result

interface = gr.Interface(
    fn=ocrImage,
    inputs=[
        gr.Image(label="Upload receipt")
    ],
    outputs="text",
    title="Image OCR",
    description="Use DeepSeek-coder:6.7b to extract text from the uploaded image.",
)

if __name__ == "__main__":
    interface.launch()
