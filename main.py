from GmailHandler import GmailHandler
from GeminiHandler import GeminiHandler

API_KEY = ""

# Fetch emails
gmail_handler = GmailHandler()
messages = gmail_handler.get_recent_messages()

# Load prompt template
with open('PROMPT_TEMPLATE.txt', 'r', encoding="utf-8") as file:
    prompt_template = file.read()

# Process emails
class Email:
    def __init__(self, subject, sender, html_content, plain_content):
        self.subject = subject
        self.sender = sender
        self.html_content = html_content
        self.plain_content = plain_content

    def __str__(self):
        return f"Sender: {self.sender}\nSubject: {self.subject}\nPlain Content: {self.plain_content}"
    
    def summarize(self, gemini_handler, prompt_template):
        """
        Summarize the email content using Gemini API.
        
        Parameters:
        gemini_handler (GeminiHandler): The Gemini API handler for generating the summary.
        rag_template (str): The RAG prompt template used to frame the content for summarization.
        
        Returns:
        str: The summarized text of the email.
        """
        # Create a prompt using the email content
        prompt = f"{prompt_template}\n{self.__str__()}\n\nOutput:\n"
        # Use GeminiHandler to get the summary
        summary = gemini_handler.generate_summary(prompt)
        return summary

email_list = [Email(m.subject, m.sender, m.html, m.plain) for m in messages]

# Generate Gemini responses
gemini_handler = GeminiHandler(api_key=API_KEY)
responses = [email.summarize(gemini_handler,prompt_template) for email in email_list]

# Format and categorize Responses
formatted = []
for i in range(len(responses)):
    if responses[i][-1] == '\n':
        formatted += [responses[i][:-1]]
    else:
        formatted += [responses[i]]
    formatted[i] = formatted[i].split('\n',1)

categorized_mails = {'1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[]}
for i in formatted:
    categorized_mails[i[0][0]] += [i[1]]

def get_str(n, dict):
    string = ""
    j = 1
    for i in dict[n]:
        string += str(j) + " : "
        string += i
        string += "\n\n"
        j += 1
    string += "\n\n"
    return string

text_result = ""

text_result += "IMPORTANT INFORMATION :\n"
text_result += get_str('2', categorized_mails)

text_result += "SUMMER INTERNSHIP :\n"
text_result += get_str('4', categorized_mails)

text_result += "VITTBI INTERNSHIP :\n"
text_result += get_str('5', categorized_mails)

text_result += "WORKSHOPS, HACKATHONS, COMPETITIONS, WEBINARS :\n"
text_result += get_str('6', categorized_mails)

text_result += "SW :\n"
text_result += get_str('3', categorized_mails)

text_result += "CLUBS AND CHAPTERS :\n"
text_result += get_str('1', categorized_mails)

text_result += "OTHER :\n"
text_result += get_str('7', categorized_mails)

text_result += "spam :\n"
text_result += get_str('8', categorized_mails)

# Printing result so streamlit app can capture stdout
print(text_result)
