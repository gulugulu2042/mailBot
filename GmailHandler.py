from simplegmail import Gmail
from simplegmail.query import construct_query

class GmailHandler:
    def __init__(self):
        self.gmail = Gmail()

    def get_recent_messages(self, n_days = 2):
        """
        Retrieve recent Gmail messages based on the number of days specified.

        This method constructs a query to fetch emails from the user's inbox that are 
        newer than a specified number of days. It uses the SimpleGmail API to retrieve 
        and return a list of email messages.

        Parameters:
        days (int): The number of days to look back for recent emails (default is 1 day).

        Returns:
        list: A list of Gmail message objects containing details such as subject, sender, 
            and content. If no emails are found, it returns an empty list.
        """
        query_params_1 = {"newer_than" : (n_days, "day")}
        messages = self.gmail.get_messages(query=construct_query(query_params_1))
        return messages