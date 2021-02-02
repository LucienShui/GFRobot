import json
import random
import typing

from dingtalkchatbot.chatbot import DingtalkChatbot


class Config:
    def __init__(self, filename: str = 'config.json'):
        with open(filename) as file:
            config: dict = json.load(file)

        self.token: str = config['token']
        self.secret: str = config['secret']
        self.sentences: typing.List[str] = config['sentences']
        self.suffix: str = config['suffix']


def main():
    config: Config = Config()
    webhook: str = f'https://oapi.dingtalk.com/robot/send?access_token={config.token}'
    robot: DingtalkChatbot = DingtalkChatbot(webhook, secret=config.secret)
    robot.send_text(msg=random.choice(config.sentences) + config.suffix, is_at_all=True)


if __name__ == '__main__':
    main()
