AI Chatbot

This is a small chatbot project made with Python and Streamlit.
It lets you chat with an AI model through a simple web interface.

Files

app.py → runs the Streamlit interface

chatbot.py → contains the chatbot logic

requirements.txt → dependencies

How to run
1. Install the packages
pip install -r requirements.txt

2. Add your API key

Create a file called .env in the project folder and put this inside:

OPENAI_API_KEY=your_key_here

3. Start the app
streamlit run app.py


Then open the link Streamlit gives you in the browser.
