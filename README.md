# Speech-Enabled-Chatbot
This code defines a chatbot that utilizes speech recognition and natural language processing (NLP) techniques to interact with users. Here's a brief overview of its functionality:

1. The code imports necessary libraries:
   - `speech_recognition` for speech recognition functionality.
   - `LlamaCpp` from the `langchain_community.llms` module for language modeling.
   - `PromptTemplate` from the `langchain.prompts` module for defining prompt templates.
   - `LLMChain` from the `langchain.chains` module for managing interactions with the language model.
   - `datetime` for handling date and time.
   - `os` for system-level operations.

2. The `speech()` function is defined to capture audio input from the user's microphone using the SpeechRecognition library. It attempts to recognize the speech using Google's speech recognition service and returns the recognized text.

3. The `speak(text)` function is defined to convert text into speech using the `say` command on macOS. It replaces single quotes in the text with escaped single quotes to prevent issues in the shell command.

4. The `chatbot()` function initializes the language model (`LlamaCpp`), defines a prompt template, and creates an `LLMChain` object to manage interactions with the prompt and model. It continuously listens for user input through speech, processes the input, and generates appropriate responses using the language model.

5. Inside the `chatbot()` function, if the user mentions "date" or "time" in their input, the chatbot retrieves the current date and time using `datetime.now()` and responds accordingly.

6. Otherwise, the chatbot invokes the language model to generate a response based on the user input.

7. The main block of the code checks if the script is executed directly and then calls the `chatbot()` function to start the chatbot.

In summary, this code creates a chatbot that can understand and respond to user input through speech using a pre-trained language model, while also providing functionalities like retrieving the current date and time.
