import time

from telethon.sync import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError

from app_config import API_ID, API_HASH

chanels = ['TelethonChat', 'ru_python_beginners', 'pydjango']

with TelegramClient('telegram_session', API_ID, API_HASH) as client:
   for channel in chanels:
        try:
            client(LeaveChannelRequest(channel))
        except FloodWaitError as fwe:
            print(fwe)
            time.sleep(fwe.seconds+20)
        except Exception as e:
            print(e)
            time.sleep(20)