import base64
import os


def base64_decode(b64_message):
    message = base64.urlsafe_b64decode(
        b64_message + '=' * (-len(b64_message) % 4)).decode(encoding='utf-8')
    return message


def save_file(base_dir, result):
    os.makedirs(base_dir, exist_ok=True)

    file_name = base_dir + '/' + result['subject'] + '.txt'
    with open(file_name, mode='w') as f:
        f.write(result['message'])
