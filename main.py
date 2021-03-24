import json
import logging
import random
import time
import typing
from datetime import datetime, timedelta

import schedule
from chinese_calendar import is_workday
from dingtalkchatbot.chatbot import DingtalkChatbot

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s:%(name)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger: logging.Logger = logging.getLogger('GFRobot')


class Config:
    def __init__(self, filename: str = 'config.json'):
        with open(filename) as file:
            json_config: dict = json.load(file)

        self.alarm_clock: list = json_config['alarm_clock']
        self.token: str = json_config['token']
        self.secret: str = json_config['secret']
        self.sentences: typing.List[str] = json_config['sentences']
        self.suffix: str = json_config['suffix']

        logger.info('config load success')


config: Config = Config()


def send_message(message: str, is_at_all: bool = False) -> dict:
    webhook: str = f'https://oapi.dingtalk.com/robot/send?access_token={config.token}'
    robot: DingtalkChatbot = DingtalkChatbot(webhook, secret=config.secret)
    result: dict = robot.send_text(msg=message, is_at_all=is_at_all)
    logger.info(f'send success, result = {json.dumps(result)}')

    return result


def check(now: datetime) -> bool:
    """
    判断此时此刻是否需要干饭
    :return:
    """
    if not is_workday(now):
        # 如果今天休息，那么不干饭
        return False

    if now.hour == 20 and not is_workday(now + timedelta(days=1)):
        # 如果此时此刻应该拿夜宵，但是明天不是工作日，那么就不提醒拿夜宵
        return False

    return True


def gan_fan():
    if check(datetime.now()):
        send_message(message=random.choice(config.sentences) + config.suffix, is_at_all=True)
    else:
        logger.info('skipped')


def setup():
    for alarm_clock in config.alarm_clock:
        schedule.every().day.at(alarm_clock).do(gan_fan)


def main():
    setup()
    json_response: dict = send_message('大家好，我是干饭机器人，我将带头干饭！')
    if json_response.get('errcode', 0) != 0:
        logger.info('service start fail')
    else:
        logger.info('service start success, cron start')
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    main()
