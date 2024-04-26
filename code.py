import speech_recognition as sr
from langchain_community.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from datetime import datetime
import os

def speech():
    if sr.Recognizer is not None:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = recognizer.listen(source)
            
            try:
                # Attempt to recognize using Dictation (might fail)
                text = recognizer.recognize_google(audio)
                # print("You said: " + text)
                return text
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

def speak(text):
    text = text.replace("'", r"'\''")  # Escape single quotes
    os.system(f"say '{text}'")

# Load the LlamaCpp language model, adjust GPU usage based on your hardware
def chatbot():
    llm = LlamaCpp(
        model_path="models/llama-2-7b-chat.Q4_0.gguf",
        n_gpu_layers=40,
        n_batch=512,  # Batch size for model processing
        verbose=False,  # Enable detailed logging for debugging
    )

    # Define the prompt template with a placeholder for the question
    template = """
    Question: {question}

    Answer:`
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])

    # Create an LLMChain to manage interactions with the prompt and model
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    print("Chatbot initialized, ready to chat...")
    while True:
        text = speech()  # Capture speech input inside the loop
        if text:
            if "date" in text.lower() or "time" in text.lower():
                current_time = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")
                print(f"Question: {text}")
                print(f"The current date and time are: {current_time}.")
                speak(text)
                speak(f"The current date and time are: {current_time}.")
            else:
                answer = llm_chain.invoke(text)
                text1 = answer['text']  # Access 'text' key directly
                print(f"Question: {text}")
                print(f"Answer: {text1}\n")
                speak(text)
                speak(text1)

if __name__ == '__main__':
    chatbot()


