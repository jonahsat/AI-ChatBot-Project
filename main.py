from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Anser the quesion below. 

Here is the conversation History: {context}

Question: {question}

Answer: 
"""

model = OllamaLLM(model="llama3")

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        else:
            result = chain.invoke({"context": context, "question": user_input})
            print("Bot: ", result)
            context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()