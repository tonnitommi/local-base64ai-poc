from robocorp.tasks import task
from robocorp import vault
import base64
import requests
import json

@task
def scan_pdf():

    base64_creds = vault.get_secret("local_base64ai_poc")
    base64_string = convert_pdf_to_base64('invoice2.pdf')

    payload = json.dumps({
        "document": "data:application/pdf;base64," + base64_string
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'ApiKey ' + base64_creds["apikey"]
    }

    response = requests.request("POST", base64_creds["url"], headers=headers, data=payload, timeout=10000)
    print(response.text)


def convert_pdf_to_base64(file_path):
    # Open the file in binary mode
    with open(file_path, 'rb') as pdf_file:
        # Read the file content
        file_content = pdf_file.read()
        # Encode the file content in base64
        base64_content = base64.b64encode(file_content)
        # Convert bytes to string
        base64_string = base64_content.decode('utf-8')
        return base64_string

