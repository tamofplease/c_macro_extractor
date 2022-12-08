import json
import requests


class HttpClient():
    def __init__(self):
        pass

    def get(self, api_url: str):
        response = requests.get(api_url, timeout=None)
        json_response = json.loads(response.text)
        return json_response


class GitApiClient():
    def __init__(self):
        self.api_client = HttpClient()
        self.base_path = 'https://api.github.com/'

    def search(self, target: str, key_word: str):
        url = self.base_path + \
            f'search/{target}?q={key_word}+language:C+stars:>=1000&sort=size&order=desc&page=1&per_page=100'
        print(url)
        return self.api_client.get(url)
