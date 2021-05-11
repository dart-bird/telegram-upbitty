from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ParseMode
import sys
import os
import pyupbit

from util.upbit_util import UpbitUtil

import json

from commands.add import Add
from commands.remove import Remove
from commands.refresh import Refresh
from commands.reset import Reset
from commands.show import Show
from commands.target import Target
from commands.getfav import Getfav
from commands.ping import Ping
from commands.targetall import TargetAll

token = os.getenv('HTTP_API')

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
upbitutil = UpbitUtil()
print("Telegram bot is ready ...")

Add.enroll(dispatcher, upbitutil)
Remove.enroll(dispatcher, upbitutil)
Refresh.enroll(dispatcher, upbitutil)
Reset.enroll(dispatcher)
Show.enroll(dispatcher, upbitutil)
Target.enroll(dispatcher, upbitutil)
TargetAll.enroll(dispatcher, upbitutil)
Getfav.enroll(dispatcher, upbitutil)
Ping.enroll(dispatcher)

updater.start_polling()
updater.idle()