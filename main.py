from __future__ import print_function

import auth
from client import ApiClient

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
# Number of emails retrieved
MAIL_COUNTS = 5


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """

    creds = auth.authenticate(SCOPES)

    client = ApiClient(creds)
    messages = client.get_mail_list(MAIL_COUNTS)

    # show message
    if not messages:
        print('No message list.')
    else:
        for message in messages:
            message_id = message['id']
            message = client.get_message(message_id)
            print(message)
            print('---------------------')


if __name__ == '__main__':
    main()
