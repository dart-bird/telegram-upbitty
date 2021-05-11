from telegram.ext import CommandHandler
from telegram import ParseMode
import json

from util.path_helper import PathHelper

USERDATA_PATH = PathHelper.get_user_data_path()

class Add():
    @staticmethod
    def enroll(dispatcher, upbitutil):
        def execute(update, context):
            
            ticker = 'KRW-' + update.message.text.split(' ')[1].upper()
            if ticker in upbitutil.get_tickers():
                f = open(USERDATA_PATH)
                user_data = json.load(f)
                favorite = user_data['favorite']
                if ticker in favorite:
                    text = ticker + " " + ", " + '이미 관심 코인으로 등록 되었어요.'
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)
                elif len(favorite) >= 10:
                    text = '**10**개 초과로 관심등록을 할 수 없어요.'
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)
                else:
                    favorite.append(ticker)
                    f = open(USERDATA_PATH,'w')
                    user_data['favorite'] = favorite
                    json.dump(user_data, f)
                    text = ticker + ", 관심코인으로 설정 했어요."
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)
            else:
                text = ticker + " 는 업비트에 상장된 코인이 아닙니다."
                context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)

        handler = CommandHandler('add', execute)
        dispatcher.add_handler(handler)
