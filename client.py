from googleapiclient.discovery import build
import base64


class ApiClient(object):

    def __init__(self, credential):
        self.service = build('gmail', 'v1', credentials=credential)

    def get_mail_list(self, limit):
        # Call the Gmail API
        results = self.service.users().messages().list(
            userId='me', maxResults=limit).execute()
        messages = results.get('messages', [])

        return messages

    def get_message(self, id):
        # Call the Gmail API
        res = self.service.users().messages().get(userId='me', id=id).execute()
        # message
        b64_message = res['payload']['parts'][0]['body']['data']
        message = base64.urlsafe_b64decode(b64_message + '=' * (-len(b64_message) % 4)).decode(encoding='utf-8')

        return message
