from telegram.ext import CommandHandler
from telegram import ParseMode
import json
from util.path_helper import PathHelper

USERDATA_PATH = PathHelper.get_user_data_path()

class Remove():
    @staticmethod
    def enroll(dispatcher, upbitutil):
        def execute(update, context):

            ticker = 'KRW-' + update.message.text.split(' ')[1].upper()
            tickers = upbitutil.get_favorite()
            if ticker in tickers:
                f = open(USERDATA_PATH, 'r')
                user_data = json.load(f)
                user_data['favorite'].remove(ticker)
                f = open(USERDATA_PATH, 'w')
                json.dump(user_data, f)
                text = '{0}, 관심코인 목록에서 삭제했어요.'.format(ticker)
            else:
                text = '{0}, 관심코인 목록에 없어요.'.format(ticker)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)

        handler = CommandHandler('remove', execute)
        dispatcher.add_handler(handler)
