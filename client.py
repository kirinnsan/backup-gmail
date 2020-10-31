from googleapiclient.discovery import build

import util


class ApiClient(object):

    def __init__(self, credential):
        self.service = build('gmail', 'v1', credentials=credential)

    def get_mail_list(self, limit, query):
        # Call the Gmail API
        results = self.service.users().messages().list(
            userId='me', maxResults=limit, q=query).execute()
        messages = results.get('messages', [])

        return messages

    def get_message(self, id):
        # Call the Gmail API
        res = self.service.users().messages().get(userId='me', id=id).execute()
        # Such as text/plain
        if 'data' in res['payload']['body']:
            b64_message = res['payload']['body']['data']
        # Such as text/html
        elif res['payload']['parts'] is not None:
            b64_message = res['payload']['parts'][0]['body']['data']
        message = util.base64_decode(b64_message)

        return message
