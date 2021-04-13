import json
import os
import requests


def main():
    toolbox = MX(api_key=os.environ.get('API_KEY'))
    remaining_requests = toolbox.usage()
    print(remaining_requests)

    result = toolbox.lookup('example.com')
    print(json.dumps(result, indent=4))


class MX:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url_base = 'https://api.mxtoolbox.com/api/v1/'
        self.headers = {
            "Accept": "application/json",
            "Authorization": self.api_key
        }

    def lookup(self, lookup_value: str, lookup_type: str = 'dns'):
        available_types = ['mx', 'a', 'dns', 'spf', 'txt', 'soa', 'ptr', 'blacklist', 'smtp', 'tcp', 'http', 'https',
                           'ping', 'trace']

        if lookup_type not in available_types:
            print(f'{lookup_type} is not a valid lookup type, available types are {available_types}')
            exit(1)

        url = self.url_base + f'Lookup/{lookup_type}/?argument={lookup_value}'
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.json())
            exit(0)

    def usage(self):
        url = self.url_base + 'Usage'
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.json())
            exit(0)


if __name__ == "__main__":
    main()
