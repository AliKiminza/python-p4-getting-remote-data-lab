import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        
        response = requests.get(URL)
        return response.content

    def load_json(self):
        URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        
        response = requests.get(URL)
        return json.loads(response.content)

get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
print(get_requester.load_json())
        