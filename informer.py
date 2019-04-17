import json
import requests
import argparse
import datetime
import os


config = None
base_url = 'https://api.telegram.org/bot'


def main():
    args = parse_args()
    push_message(args.message)


def get_config():
    global config
    if not config:
        file = os.path.join(os.path.dirname(__file__), 'tconf.json')
        with open(file, 'r') as f:
            config = json.load(f)
            print(config)
    return config


def push_message(text):
    conf = get_config()
    url = f'{base_url}{conf["bot_token"]}/sendMessage'
    data = {
        'chat_id': conf['channel_id'],
        'text': text,
    }
    return requests.post(url, data=data, proxies=conf['proxies'])


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--message', required=True, help='Message text')
    return p.parse_args()


if __name__ == '__main__':
    main()
