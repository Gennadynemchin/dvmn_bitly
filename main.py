import argparse
import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
from requests.models import HTTPError


def is_bitlink(link, auth) -> bool:
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    response = requests.get(url, headers={'Authorization': auth})
    return response.ok


def shorten_link(link, auth):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    payload = {'long_url': link}
    response = requests.post(url, json=payload, headers={'Authorization': auth})
    response.raise_for_status()
    decoded_response = response.json()
    return decoded_response["link"]


def count_click(bitlink, auth):
    url_count = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response_count = requests.get(url_count, headers={'Authorization': auth})
    response_count.raise_for_status()
    decoded_response = response_count.json()
    return decoded_response['total_clicks']


def main():
    load_dotenv()
    BITOKEN = os.getenv('BITOKEN')
    parser = argparse.ArgumentParser(description='Bitly command line application')
    parser.add_argument('-l', '--bitlink', help='enter your link here', type=str)
    args = parser.parse_args()
    if args.bitlink is not None:
        link = args.bitlink
    else:
        link = input('Enter a link: ')
    parsed_link = urlparse(link)
    link2func = f'{parsed_link.hostname}{parsed_link.path}'
    if is_bitlink(link2func, BITOKEN):
        try:
            print(f'Total clicks: {count_click(link2func, BITOKEN)}')
        except HTTPError as err:
            print(err)
    else:
        try:
            print(shorten_link(link, BITOKEN))
        except HTTPError as err:
            print(err)


if __name__ == '__main__':
    main()
