**📧 mailBot - VIT Email Summarizer App**
This project is a Streamlit web application that processes your recent emails from Gmail, summarizes them using a Gemini AI model, and displays the summarized emails on the UI. The app fetches emails via the Gmail API and uses a predefined prompt to interact with the Gemini AI for summarization.
The prompt template is specially made to categorize and summarize mails from my university (VIT uni - THEY SPAM A LOT). You can modify PROMPT_TEMPLATE.txt to fit your needs.

**🌟 Features**
Fetches emails sent and recieved inthe last day using the Gmail API.
Summarizes emails with Gemini AI (Gemini-1.5-flash model).
Displays the summarized emails in a user-friendly interface.
Simple and intuitive UI built with Streamlit.

**🚀 Getting Started**
1. Clone the repository:

git clone https://github.com/gulugulu2042/mailBot
cd mailBot

**2. Install dependencies:**
Make sure you have Streamlit, the Gmail API library, and Gemini API configured properly.

pip install -r requirements.txt

**3. Set up API keys:**

Gmail API:
Follow Google's guide to enable the Gmail API and download client_secret.json. (If the file has some other name, rename it to client_secret.json)
Place the client_secret.json file in your project directory.
Gemini API:
Obtain your API key from the Gemini API.
Add your API key to main.py.
6. Run the Streamlit app:
python -m streamlit run app.py 

The app will start and open in your browser. You can now process your emails by clicking the "Process Emails" button and authenticating your google account.

**✨ How It Works**
Gmail Integration:

The app uses the Gmail API to fetch your recent emails. You can customize the query to filter emails by date, sender, or other attributes.
Email Summarization:

Each fetched email is passed to the Gemini AI model, which uses a predefined RAG Prompt (loaded from PROMPT_TEMPLATE.txt) to generate a concise summary of the email.
Streamlit UI:

The user interacts with the app through a simple web UI built using Streamlit. A button triggers the email processing and displays the summarized content.

**📄 Requirements**
Python 3.7 or higher
Gmail API access
Gemini AI API key

**🔧 Configuration**
Gmail API Setup:
Visit the Gmail API Quickstart.
Enable the API and download the credentials.json file.
Place the credentials.json file in the root directory of this project.
Gemini AI Setup:
Obtain your API key from Gemini.
Add the API key to the main.py file like so:
API_KEY = "YOUR_GEMINI_API_KEY"
Modify the Email Query:
To modify the email fetch query, you can update the parameters in GmailHandler.py to fetch emails based on your preferences:

query_params = {
    "newer_than": (1, "day")  # Fetch emails from the last 1 day
}

**🧩 Customization**
Prompt Customization: You can modify the prompt in PROMPT_TEMPLATE.txt to fit your summarization style. Simply edit the template and adjust how the emails are summarized by the Gemini AI.

Email Filters: You can easily adjust the Gmail API query to fetch specific emails by changing the query parameters in main.py.

**🤝 Contributions**
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

**📧 Contact**
For any inquiries or suggestions, feel free to reach out at: gokul26.09.2004@gmail.com.

**🙌 Acknowledgments**
Google Gmail API
Gemini AI
Streamlit

Enjoy your email summarization with AI! 😊
