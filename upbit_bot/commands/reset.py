from telegram.ext import CommandHandler
from telegram import ParseMode
import json
import os
from util.path_helper import PathHelper

USERDATA_PATH = PathHelper.get_user_data_path()

class Reset():
    @staticmethod
    def enroll(dispatcher):
        def execute(update, context):
            f = open(USERDATA_PATH)
            user_data = json.load(f)
            user_data['favorite'].clear()
            f = open(USERDATA_PATH,'w')
            json.dump(user_data, f)
            text = '관심 코인 목록을 초기화 했어요.'
            context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)

        handler = CommandHandler('reset', execute)
        dispatcher.add_handler(handler)
