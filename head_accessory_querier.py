import requests
import json

def get_pudgy_penguin_head_accessory(slug, api_key):
    url = f"https://api.opensea.io/api/v2/collections/{slug}"
    headers = {
        "Accept": "application/json",
        "X-API-KEY": api_key
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve head accessory data. Status code: {response.status_code}")
        return None

def get_pudgy_penguin_traits(slug, api_key):
    url = f"https://api.opensea.io/api/v2/traits/{slug}"
    headers = {
        "Accept": "application/json",
        "X-API-KEY": api_key
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve traits data. Status code: {response.status_code}")
        return None

def save_json_to_file(data, filename):
    if data:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data successfully saved to {filename}")
    else:
        print(f"No data to save for {filename}")

slug = "pudgypenguins"
api_key = "a99d654a780e4998bd4566e2e24b9d2c"  # Replace with your actual API key

# Retrieve and save head accessory data
head_accessory_data = get_pudgy_penguin_head_accessory(slug, api_key)
save_json_to_file(head_accessory_data, "head_accessory.json")

# Retrieve and save traits data
traits_data = get_pudgy_penguin_traits(slug, api_key)
save_json_to_file(traits_data, "traits.json")
