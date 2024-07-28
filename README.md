# Download Ollama

1. Download and install Ollama from: https://ollama.com/

2. Test if Ollama is working by typing `ollama` in Command Prompt

# Download and Test the model

3. Download the LLM with the command: 
    $ `ollama pull llama3`
   (You can find the list of models at https://github.com/ollama/ollama)
> [!NOTE]
> Ensure you have an Nvidia GPU and at least 8GB RAM. Also, check the requirements for each model based on the parameter.


5. Test the model by typing: 
    $ `ollama run llama3`

# Project Creation

6. Make a folder and open it in any IDE (for eg. VSCode)

7. Open the terminal and create a virtual environment by typing: 
    $ `python -m venv chatbotenv`

8. Activate the virtual environment by typing: 
    $ `chatbotenv\Scipts\activate`
> [!NOTE]
> The above command only works in Command Prompt, not in PowerShell.

# Install Requirements

10. Install the requirements by running:
    $ `pip install -r requirements.txt`

# Run the Chatbot

11. Run the AI Chatbot by typing:
    $ `python main.py`

