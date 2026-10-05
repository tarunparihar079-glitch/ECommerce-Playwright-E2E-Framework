import requests
import json
import random
import os

def get_real_user_from_api():
    user_id = random.randint(1,10)
    api_url = f"{os.getenv('REQRES_API_URL').strip()}{user_id}"

    print(f"\n[INFO] Fetching data from API: {api_url}")

    response = requests.get(api_url)
    assert response.status_code == 200, f"API failed! Status code: {response.status_code}"

    raw_text_data = response.text
    parsed_json = json.loads(raw_text_data)

    first_name = parsed_json['data']['first_name']
    last_name = parsed_json['data']['last_name']
    email_id = parsed_json['data']['email']

    print(f"[INFO] User data retrieved: {first_name} {last_name}, {email_id}")

    return first_name, last_name, email_id