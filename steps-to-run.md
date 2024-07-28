1. Download and install Ollama from: https://ollama.com/

2. Test if Ollama is working by typing ollama in Command Prompt

3. Download the LLM with the command: 
    $ ollama pull llama3
    (You can find the list of models in https://github.com/ollama/ollama)
    [Note: Make sure you have a Nvidia GPU and atleast 8GB ram. Also check the requirements for each model based on the parameter.]

4. Test the model by typing: 
    $ ollama run llama3

5. Make a folder and open it in any IDE (for eg. VSCode)

6. Open terminal and create a virtual environment by typing: 
    $ python -m venv chatbotenv

7. Activate the virtual environment by typing: 
    $ chatbotenv\Scipts\activate
    [Note: The above command only works in Command Prompt, not in PowerShell]

8. Install the requirements by running:
    $ pip install -r requirements.txt

9. Run the AI Chatbot by typing:
    $ python main.py

