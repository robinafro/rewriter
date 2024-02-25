import requests
import json

# Define the URL
url = 'https://api.zerogpt.com/api/transform/grammarCheck'

# Define headers with Content-Type
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'Content-Type': 'application/json',
    'Origin': 'https://www.zerogpt.com',
    'Referer': 'https://www.zerogpt.com/',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Gpc': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

def send_request(input_text):
    # Define the payload as a dictionary
    payload = {'string': input_text, 'tone': "teenager"}

    # Convert payload to JSON format
    json_payload = json.dumps(payload)

    # Send the POST request with JSON payload and headers
    response = requests.post(url, data=json_payload, headers=headers)

    # Check the response status
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("POST request failed with status code:", response.status_code)
        return None