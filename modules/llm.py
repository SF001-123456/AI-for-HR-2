import ollama
import re

def ollama_generate_response(prompt):
    response = ollama.chat(
        model="gemma2",
        messages=[{"role": "user", "content": prompt}],
    )

    response_content = response["message"]["content"]
    final_answer = re.sub(r"<think>.*?</think>", "", response_content, flags=re.DOTALL).strip()

    return final_answer

def ollama_llm(question, context):
    formatted_prompt = f"Question: {question}\n\nContext: {context}"

    return ollama_generate_response(formatted_prompt)

